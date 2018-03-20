"""
其他类型的方法放在这里
"""

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
        print('--- {} done ---'.format(str(func)))
        return result
    return _logger
