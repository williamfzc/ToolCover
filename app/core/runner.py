"""
这个模块负责确保inside app的正常运作
"""
import subprocess
import os
import fcntl
import psutil
import time
from .utils import singleton, func_logger, logger
from config import *
from collections import namedtuple


# 返回给上层的结果类
RunnerResponse = namedtuple('RunnerResponse', ('status', 'result'))


def is_runnable():
    """
    检查嵌入的app是否符合规范

    :return: True or Error
    """
    # packages目录下所有的文件夹
    target_app_list = [
        each for each in os.listdir(PACKAGE_PATH)
        if os.path.isdir(os.path.join(PACKAGE_PATH, each))
    ]

    # 是否存在目标文件夹
    if APP_DIR not in target_app_list:
        raise FileNotFoundError('No target app found in {}.'.format(PACKAGE_PATH))
    target_app_path = os.path.join(PACKAGE_PATH, APP_DIR)

    # 在嵌入的app内查看是否具备必有文件
    # 如run.py和README.md
    file_list = os.listdir(target_app_path)
    search_result = [
        each for each in NECESSARY_FILE_LIST
        if each not in file_list
    ]

    if search_result:
        error_message = 'required files not found: {}'.format(','.join(search_result))
        raise FileNotFoundError(error_message)
    else:
        return target_app_path


def get_app_process():
    """
    获取运行子程序的进程对象，供交互

    :return: subprocess object
    """
    target_app_path = is_runnable()
    entry_path = os.path.join(target_app_path, APP_ENTRY)
    os.chmod(entry_path, 0b111101101)
    app_instance = subprocess.Popen(
        [RUNNER_PATH, os.path.join(target_app_path, APP_ENTRY)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=RUN_ON_SHELL
    )
    flags = fcntl.fcntl(app_instance.stdout, fcntl.F_GETFL)
    fcntl.fcntl(app_instance.stdout, fcntl.F_SETFL, flags | os.O_NONBLOCK)
    return app_instance


def get_readme():
    target_app_path = is_runnable()
    doc_path = os.path.join(target_app_path, APP_DOC)
    with open(doc_path) as doc_file:
        result = doc_file.read()
    return result


@singleton
class SubApp(object):
    """
    从内层应用的stdout读数据，向他的stdin写数据
    """
    def __init__(self):
        self.app_instance = get_app_process()
        self.process_item = psutil.Process(self.app_instance.pid)
        self.last_write_time = None

    def is_expired(self):
        """ 两次请求之间是否已经超时 """
        now_time = time.time()
        if self.last_write_time:
            time_difference = now_time - self.last_write_time
            if time_difference > TIME_OUT:
                return True
            else:
                self.last_write_time = now_time
                return False
        else:
            self.last_write_time = now_time
            return False

    @func_logger
    def read(self):
        """ 读内嵌app输出的数据 """
        # TODO: delay time needs to be more precise
        # really strange. without this, first page will empty
        time.sleep(0.1)

        # 超时
        if self.is_expired():
            self.stop()
            return RunnerResponse(status='timeout', result=None)
        # 已经结束
        if self.is_done():
            status = 'end'
        # 继续
        else:
            status = 'normal'

        result_list = [
            each.decode(DEFAULT_TEST_ENCODING).strip()
            for each in self.app_instance.stdout.readlines()
        ]

        logger.log_data('from runner\'s read: {}'.format(str(result_list)))
        return RunnerResponse(status=status, result=result_list)

    @func_logger
    def write(self, content):
        """ 向内嵌app传递数据 """
        if self.is_expired():
            return False
        if content is None:
            content = ''
        self.app_instance.stdin.write(bytes(str(content) + os.linesep, DEFAULT_TEST_ENCODING))
        self.app_instance.stdin.flush()

    def is_done(self):
        """ return if subprocess ended """
        # make sure poll's return is correct
        # poll() will delay
        # TODO: delay time needs to be more precise
        time.sleep(0.1)
        if self.app_instance.poll() is not None:
            return True
        else:
            return False

    def stop(self):
        """ 停止内层应用 """
        if not self.app_instance:
            return True
        # 还没结束的话要杀掉
        if self.app_instance.poll() is None:
            self.app_instance.kill()
        self.app_instance = None

    def reset(self):
        """ 重启内层应用 """
        self.stop()
        self.__init__()


# 初始化
sub_app = SubApp()
