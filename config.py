import os


# 根目录
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# 关键目录
APP_ROOT_PATH = os.path.join(PROJECT_PATH, 'app')
CORE_PATH = os.path.join(APP_ROOT_PATH, 'core')
PACKAGE_PATH = os.path.join(APP_ROOT_PATH, 'packages')
TEMPLATE_PATH = os.path.join(APP_ROOT_PATH, 'templates')

# python目录 根据实际修改
PYTHON_PATH = os.path.join(PROJECT_PATH, 'venv', 'bin', 'python3.6')

# 入口
APP_ENTRY = 'run.py'
# 文档
APP_DOC = 'README.md'

# 嵌入app内必要的文件
NECESSARY_FILE_LIST = [
    APP_ENTRY,
    APP_DOC
]

__all__ = [
    PROJECT_PATH,
    APP_ROOT_PATH,
    CORE_PATH,
    PACKAGE_PATH,
    TEMPLATE_PATH,
    NECESSARY_FILE_LIST
]