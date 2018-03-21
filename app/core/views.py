"""
路由层

1. 从form_handler得到Form类，实例化后由jinja2+wtforms渲染
2. 在用户填写完毕之后会得到一个有内容的form实例，将实例传递给form_handler处理

"""
from ..core import core_blueprint
from flask import render_template, redirect, url_for
from .form_handler import *
from .utils import logger
from .runner import sub_app


def handle_form(stop_signal, object_need_handle):
    # 两种情况
    # 1. 如果已经停止，需要重定向到end路由，object_need_handle的类型是string
    # 2. 如果还没停止，object_need_handle的值为FlaskForm

    if stop_signal:
        return 'end', redirect(url_for('.end', content=object_need_handle))
    else:
        return 'form', object_need_handle


@core_blueprint.route('/start', methods=['GET', 'POST'])
def start():
    """ 主路由，所有与子进程的交互都在这里完成 """
    result_type, result_from_handler = handle_form(*load_form())
    logger.info((result_type, str(result_from_handler)))

    if result_type == 'end':
        # 是个Response对象
        return result_from_handler
    else:
        # 是个Form对象，则生成实例
        form = result_from_handler()

    # 处理还没停止的情况
    if form.validate_on_submit():
        # 如果用户提交了表单，Form类需要根据返回作相应改变
        user_input = form.content.data
        result_type, result_from_handler = handle_form(*load_form(user_input))
        if result_type == 'end':
            # 是个Response对象
            return result_from_handler
        else:
            # 是个Form对象，则生成实例
            new_form = result_from_handler()
            return render_template('app.html', form=new_form)

    return render_template('app.html', form=form)


@core_blueprint.route('/', methods=['GET', 'POST'])
def index():
    sub_app.reset()
    form = build_form(empty_form=True)()

    # 用户点了开始
    if form.validate_on_submit():
        return redirect(url_for('.prepare'))

    return render_template(
        'index.html',
        content=get_description(),
        form=form
    )


@core_blueprint.route('/end/')
@core_blueprint.route('/end/<content>')
def end(content=None):
    return render_template('end.html', content=content)


@core_blueprint.route('/prepare')
def prepare():
    # 放置准备阶段的逻辑
    return redirect(url_for('.start'))
