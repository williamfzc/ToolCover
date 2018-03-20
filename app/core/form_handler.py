"""
主要有两个功能

1. 接收inside app的output，将其转换成Form对象后提交给路由
2. 将路由得到的form实例解包，把数据传递给inside app

"""
from .runner import sub_app
from .utils import func_logger
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


def _build_form(hints_str):
    """ 动态构建Form类

    :param hints_str: 输入框的提示语
    :return: Form类
    """
    class Result(FlaskForm):
        content = StringField(hints_str, validators=[DataRequired()])
        submit = SubmitField('Commit')

    return Result


@func_logger
def load_form(request_content=None):
    """ 根据用户的输入内容向下一层发送请求并等待反馈，再构建新的Form返回给上层 """

    # 向下层递交请求
    inside_output = sub_app.request_with(request_content)
    # 用反馈内容构建新的Form
    form_cls = _build_form(inside_output)

    global InputForm
    InputForm = form_cls
    return InputForm


