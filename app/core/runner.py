"""
这个模块负责确保inside app的正常运作
"""
import subprocess
import os
import time
import fcntl
import select
from config import PACKAGE_PATH, NECESSARY_FILE_LIST, APP_ENTRY, PYTHON_PATH, DEFAULT_CODE


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

    if target_app_list:
        # todo: 如果有多个app联动的场景，需要考虑新逻辑
        target_app_path = os.path.join(PACKAGE_PATH, target_app_list[0])
    else:
        raise FileNotFoundError('No app found in {}.'.format(PACKAGE_PATH))

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
        [PYTHON_PATH, os.path.join(target_app_path, APP_ENTRY)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    flags = fcntl.fcntl(app_instance.stdout, fcntl.F_GETFL)
    fcntl.fcntl(app_instance.stdout, fcntl.F_SETFL, flags | os.O_NONBLOCK)
    return app_instance


class SubApp(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.app_instance = get_app_process()

    def read(self):
        """ 从内嵌app中读数据 """
        result = []
        while True:
            line = self.app_instance.stdout.readline()
            if not line:
                break
            result.append(str(line, encoding=DEFAULT_CODE))
        return '\n'.join(result)

    def write(self, content):
        """ 向内嵌app传递数据 """
        self.app_instance.stdin.write(content.encode(DEFAULT_CODE))
        self.app_instance.stdin.flush()

    def stop(self):
        """ 停止内层应用 """
        self.app_instance.kill()
        self.app_instance = None

    def reset(self):
        """ 重启内层应用 """
        self.stop()
        self.__init__()

    def wait_data(self):
        """ 阻塞直到内层应用有消息返回 """
        # TODO: IO不能用，只有第一次能成功
        pass

# 初始化
sub_app = SubApp()
