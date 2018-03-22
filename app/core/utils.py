"""
其他类型的方法放在这里
"""
import logging
import sys


# 单例，获取logger的方法
def get_logger():
    if hasattr(globals(), 'logger'):
        return globals()['logger']

    # 获取logger实例
    logger = logging.getLogger()

    # 指定logger输出格式
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.formatter = formatter

    # 等级
    logger.setLevel(logging.INFO)

    # 添加handler
    logger.addHandler(console_handler)
    globals()['logger'] = logger
    return logger


# 单例装饰器
def singleton(cls):
    cls_dict = dict()

    def _singleton(*args, **kwargs):
        # ensure it is hashable
        cls_name = str(cls)
        if cls_name not in cls_dict:
            cls_dict[cls_name] = cls(*args, **kwargs)
        return cls_dict[cls_name]
    return _singleton


# 日志装饰器
def func_logger(func):
    def _logger(*args, **kwargs):
        result = func(*args, **kwargs)
        func_name = func.__name__
        logger.info('FUNCTION {} DONE'.format(func_name))
        return result
    return _logger


logger = get_logger()
