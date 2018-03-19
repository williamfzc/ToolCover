"""
这个模块负责确保inside app的正常运作
"""
import subprocess
import os
from config import PACKAGE_PATH, NECESSARY_FILE_LIST, APP_ENTRY, PYTHON_PATH


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
    # 如果已经构建好了就直接返回，单例模式
    if hasattr(globals(), 'sub_app'):
        return globals()['sub_app']

    target_app_path = is_runnable()
    entry_path = os.path.join(target_app_path, APP_ENTRY)
    os.chmod(entry_path, 0b111101101)
    app_instance = subprocess.Popen(
        [PYTHON_PATH, os.path.join(target_app_path, APP_ENTRY)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return app_instance


def read_sub_app():
    """ 从内嵌app中读数据 """
    return '\n'.join([str(line[:-1], encoding='utf-8') for line in sub_app.stdout.readlines()])


def write_sub_app(content):
    """ 向内嵌app传递数据 """
    sub_app.stdin.write(content)


# init
sub_app = get_app_process()
sub_app.read = read_sub_app
sub_app.write = write_sub_app
