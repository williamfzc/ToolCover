"""
主要有两个功能

1. 接收inside app的output，将其转换成Form对象后提交给路由
2. 将路由得到的form实例解包，把数据传递给inside app

"""
from .runner import sub_app, get_readme
from .utils import func_logger, logger
from markdown import markdown
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from collections import OrderedDict, namedtuple
import os


last_output_from_inside = None
TYPE_LIST = {
    'multi-list': SelectMultipleField,
    'single-list': SelectField
}
HandlerResponse = namedtuple('HandlerResponse', ('stop_signal', 'form', 'other_content'))


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
            cls_dict['content'] = StringField(
                '', validators=[DataRequired()],
                render_kw={
                    "placeholder": hints_str,
                    "value": ''
                }
            )

    # 添加next按钮
    cls_dict['next'] = SubmitField('Next')
    return type('InputForm', (FlaskForm,), cls_dict)


@func_logger
def load_form(request_content=None):
    """ 根据用户的输入内容向下一层发送请求并等待反馈，再构建新的Form返回给上层 """
    global last_output_from_inside

    # 如果用户输入为空说明是初始化，不向内层应用写数据，只读数据
    # 路由层已经保证了所有用户的输入都不为空
    if request_content:
        sub_app.write(request_content)
    inner_output = sub_app.read()

    # 是否为刷新（无输出无输入）
    if not inner_output and request_content is None:
        logger.log_status('refresh page')
        inner_output = last_output_from_inside
    else:
        # 记录上一次的输出以便特殊情况重新渲染
        last_output_from_inside = inner_output

    # 先查看是否超时
    if isinstance(inner_output, bytes) and b'timeout' == inner_output:
        logger.log_status('timeout')
        time_out_msg = 'Time out. Please restart.'
        return HandlerResponse(stop_signal=True, form=None, other_content=time_out_msg)
    else:
        # 常规内容，string list
        # 取最后一句作为input框提示
        # 如果只有一句，那就以那句为提示
        inner_output_length = len(inner_output)
        if inner_output_length >= 1:
            # 再查看是否已经结束
            # 两种情况统一处理
            # 1. 结束了且没有输出
            # 2. 结束了有输出，需要信息展示
            if inner_output[-1] == b'end':
                end_msg = os.linesep.join(inner_output[:-1])
                logger.log_status('normal end with msg: {}'.format(end_msg))
                return HandlerResponse(stop_signal=True, form=None, other_content=end_msg)

            logger.log_status('normal continue')
            input_tips = inner_output[-1]
            other_content = ''.join(inner_output[:-1]) if inner_output_length > 1 else ''

            # 构建Form类
            form_cls = build_form(input_tips)
            return HandlerResponse(stop_signal=False, form=form_cls, other_content=other_content)
        # 没输出，正常来说不会来到这里
        else:
            logger.log_status('no output')
            end_msg = os.linesep.join(inner_output[:-1])
            return HandlerResponse(stop_signal=True, form=None, other_content=end_msg)


def get_description():
    """ get html from README """
    return markdown(get_readme())
