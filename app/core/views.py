"""
路由层

1. 从form_handler得到Form类，实例化后由jinja2+wtforms渲染
2. 在用户填写完毕之后会得到一个有内容的form实例，将实例传递给form_handler处理

"""
from ..core import core_blueprint
from flask import render_template, redirect
from .form_handler import *


@core_blueprint.route('/', methods=['GET', 'POST'])
def start():
    """ 主路由，所有与子进程的交互都在这里完成 """
    form = load_form()()

    if form.validate_on_submit():
        parse_form(form)
        return redirect('core_blueprint.start')

    return render_template('app.html', form=form)


@core_blueprint.route('/entry')
def index():
    # TODO: 将markdown的内容放到这里 并提供程序入口
    from .runner import sub_app
    sub_app.reset()
    return 'Still building...'


