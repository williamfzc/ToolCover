from .utils import build_form


# TODO: 考虑一下是否真的需要API
def need_value(hints_str, value_type=None):
    # 替代input的存在

    # 主要功能应该将input拆解成两部分
    # 将需要展示的信息提前拿出来渲染
    # 输入由表单提交

    # 这个部分应该能够动态构建表单
    build_form(hints_str)
    # 需要拿到用户传入UI的结果