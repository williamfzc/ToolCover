from .runner import sub_app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


def read_sub_app():
    """ 从内嵌app中读数据 """
    return '\n'.join([str(line[:-1], encoding='utf-8') for line in sub_app.stdout.readlines()])


def write_sub_app(content):
    """ 向内嵌app传递数据 """
    sub_app.stdin.write(content)


def add_tag(origin_str, tag_type):
    # 给str加html标签
    # TODO：需要看一下为什么不生效
    tag_list = ['h1', 'h2', 'p']
    if tag_type not in tag_list:
        raise TypeError('You should only use these tag: {}'.format(str(tag_list)))
    tag_template = '<{tag}> {ori_str} </{tag}>'
    return tag_template.format(
        tag=tag_type,
        ori_str=origin_str
    )


class DefaultForm(FlaskForm):
    submit = SubmitField('Commit')


form_class_template = '''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    content = StringField('{hints}', validators=[DataRequired()])
    submit = SubmitField('Commit')

'''


def build_form(hints_str, value_type=None):
    # 动态构建表单类
    define_str = form_class_template.format(hints=hints_str)
    exec(define_str, globals())
    return globals()['InputForm']
