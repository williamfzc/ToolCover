import os


PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
APP_ROOT_PATH = os.path.join(PROJECT_PATH, 'app')
CORE_PATH = os.path.join(APP_ROOT_PATH, 'core')
PACKAGE_PATH = os.path.join(APP_ROOT_PATH, 'packages')
TEMPLATE_PATH = os.path.join(APP_ROOT_PATH, 'templates')


__all__ = [
    PROJECT_PATH,
    APP_ROOT_PATH,
    CORE_PATH,
    PACKAGE_PATH,
    TEMPLATE_PATH
]
