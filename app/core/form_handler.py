"""
主要有两个功能

1. 接收inside app的output，将其转换成Form对象后提交给路由
2. 将路由得到的form实例解包，把数据传递给inside app

"""
from .runner import sub_app

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


def _build_form(hints_str):
    """ 动态构建Form类

    :param hints_str: 输入框的提示语
    :return: Form类
    """
    class InputForm(FlaskForm):
        content = StringField(hints_str, validators=[DataRequired()])
        submit = SubmitField('Commit')

    return InputForm


def load_form():
    inside_output = sub_app.read()
    form_cls = _build_form(inside_output)
    print(isinstance(form_cls, FlaskForm))
    return form_cls


def parse_form(form_object):
    inside_input = form_object.content.data
    sub_app.write(inside_input)


__all__ = ['load_form', 'parse_form']
