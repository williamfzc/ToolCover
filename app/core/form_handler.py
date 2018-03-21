"""
主要有两个功能

1. 接收inside app的output，将其转换成Form对象后提交给路由
2. 将路由得到的form实例解包，把数据传递给inside app

"""
from .runner import sub_app, get_readme
from .utils import func_logger
from markdown import markdown
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from collections import OrderedDict


last_output_from_inside = None
TYPE_LIST = {
    'multi-list': SelectMultipleField,
    'single-list': SelectField
}


def is_special_type(input_str):
    # seems like:
    # 'multi-list|description|choice1%choice2%choice3'
    if '|' not in input_str:
        return False
    type_name, *_, = input_str.split('|')
    if type_name in TYPE_LIST:
        return True
    else:
        return False


def parse_special_str(special_str):
    """ parse special str, and turn it into special widget """
    # only support single list and multi list now
    type_name, desc_str, choice_str = special_str.split('|')
    type_cls = TYPE_LIST[type_name]
    choice_list = choice_str.split('%')
    args_list = [(i, i) for i in choice_list]
    return type_cls(desc_str, choices=args_list, validators=[DataRequired()])


def build_form(hints_str=None):
    """ 动态构建Form类

    :param hints_str: 输入框的提示语
    :return: Form类
    """
    # 最后用于type构建类的字典
    cls_dict = OrderedDict()

    # 是否有特殊控件
    if hints_str is not None:
        if is_special_type(hints_str):
            cls_dict['content'] = parse_special_str(hints_str)
        # 常规操作
        else:
            cls_dict['content'] = StringField(hints_str, validators=[DataRequired()])

    # 添加next按钮
    cls_dict['next'] = SubmitField('Next')
    InputForm = type('InputForm', (FlaskForm,), cls_dict)
    return InputForm

@func_logger
def load_form(request_content=None):
    """ 根据用户的输入内容向下一层发送请求并等待反馈，再构建新的Form返回给上层 """
    # 是否结束的标志
    stop_signal = False

    # 如果用户输入为空说明是初始化，不向内层应用写数据，只读数据
    # 路由层已经保证了所有用户的输入都不为空
    if request_content:
        sub_app.write(request_content)
    inner_output = sub_app.read()

    # 内层app是否已经执行完了
    # 两种情况统一处理
    # 1. 结束了且没有输出
    # 2. 结束了有输出，需要信息展示
    if sub_app.is_done():
        stop_signal = True
        object_need_handle = inner_output
    else:
        global last_output_from_inside
        # 还没结束但输入为空，也没有返回值，说明是刷新，沿用上次结果
        if request_content is None and inner_output is None:
            inner_output = last_output_from_inside
        # 有输入，还没结束，常规场景
        # 用反馈内容构建新的Form
        else:
            # 记录上一次的输出以便特殊情况重新渲染
            last_output_from_inside = inner_output
        # 构建Form类
        object_need_handle = build_form(inner_output)

    return stop_signal, object_need_handle


def get_description():
    """ get html from README """
    return markdown(get_readme())
