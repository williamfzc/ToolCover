import os


# root directory
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# important directory
APP_ROOT_PATH = os.path.join(PROJECT_PATH, 'app')
CORE_PATH = os.path.join(APP_ROOT_PATH, 'core')
PACKAGE_PATH = os.path.join(APP_ROOT_PATH, 'packages')
TEMPLATE_PATH = os.path.join(APP_ROOT_PATH, 'templates')

# SECRET_KEY
SECRET_KEY = 'test only'

# ----- user-defined below -----

# path to run your app
# eg: if command is 'python3 test.py', RUNNER_PATH is python3.
RUNNER_PATH = os.path.join(PROJECT_PATH, 'venv', 'bin', 'python3')

# run on shell or not
RUN_ON_SHELL = False

# app name
APP_NAME = 'Example in ToolCover'
# entry of your app
APP_ENTRY = 'run.py'
# name of your document
APP_DOC = 'README.md'

# necessary file list
NECESSARY_FILE_LIST = [
    APP_ENTRY,
    APP_DOC
]

# default text encoding
DEFAULT_TEST_ENCODING = 'utf-8'

# expired time if no request
TIME_OUT = 60
