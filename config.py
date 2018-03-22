import os


# 根目录
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# 关键目录
APP_ROOT_PATH = os.path.join(PROJECT_PATH, 'app')
CORE_PATH = os.path.join(APP_ROOT_PATH, 'core')
PACKAGE_PATH = os.path.join(APP_ROOT_PATH, 'packages')
TEMPLATE_PATH = os.path.join(APP_ROOT_PATH, 'templates')

# SECRET_KEY
SECRET_KEY = 'guess what'

# ----- 以下为自定义部分 -----

# 运行方式 根据实际修改
# 如果希望运行.exe等其他文件，可自行配置其他运行器
RUNNER_PATH = os.path.join(PROJECT_PATH, 'venv', 'bin', 'python3')

# 是否使用shell运行
# TODO: 目前使用shell运行python会有io问题，后续关注
RUN_ON_SHELL = False

# 应用名称
APP_NAME = 'Example in ToolCover'
# 入口
APP_ENTRY = 'run.py'
# 文档
APP_DOC = 'README.md'

# 嵌入app内必要的文件，必须要有的是入口与文档
NECESSARY_FILE_LIST = [
    APP_ENTRY,
    APP_DOC
]

# 默认文本编码
DEFAULT_TEST_ENCODING = 'utf-8'

# 用户无输入一段时间后会关闭内层app
# 超时时间
TIME_OUT = 60
