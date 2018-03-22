"""
路由层

1. 从form_handler得到Form类，实例化后由jinja2+wtforms渲染
2. 在用户填写完毕之后会得到一个有内容的form实例，将实例传递给form_handler处理

"""
from ..core import core_blueprint
from flask import render_template, redirect, url_for, session
from .handler import *
from config import APP_NAME
from .runner import sub_app


@core_blueprint.route('/start', methods=['GET', 'POST'])
def start():
    """ 主路由，所有与子进程的交互都在这里完成 """
    handler_response = load_form()
    # 如果进程结束
    if handler_response.stop_signal:
        session['end_content'] = handler_response.other_content
        return redirect(url_for('.end'))
    form = handler_response.form()
    desc = markdown(handler_response.other_content)

    # 处理还没停止的情况
    if form.validate_on_submit():
        # 如果用户提交了表单，Form类需要根据返回作相应改变
        user_input = form.content.data
        handler_response = load_form(user_input)
        # 如果进程结束
        if handler_response.stop_signal:
            session['end_content'] = handler_response.other_content
            return redirect(url_for('.end'))
        form = handler_response.form()
        desc = markdown(handler_response.other_content)

    return render_template('app.html', form=form, app_name=APP_NAME, description=desc)


@core_blueprint.route('/', methods=['GET', 'POST'])
def index():
    sub_app.reset()
    form = build_form()()

    # 用户点了开始
    if form.validate_on_submit():
        return redirect(url_for('.prepare'))

    return render_template(
        'index.html',
        content=get_description(),
        form=form,
        app_name=APP_NAME
    )


@core_blueprint.route('/end/')
def end():
    content = session['end_content']
    if content:
        content = markdown(content)
    return render_template('end.html', content=content)


@core_blueprint.route('/prepare')
def prepare():
    # 放置准备阶段的逻辑
    return redirect(url_for('.start'))
