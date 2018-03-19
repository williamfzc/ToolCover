"""
路由层

1. 从form_handler得到Form类，实例化后由jinja2+wtforms渲染
2. 在用户填写完毕之后会得到一个有内容的form实例，将实例传递给form_handler处理

"""
from ..core import core_blueprint
from flask import render_template
from .form_handler import *


@core_blueprint.route('/')
def index():
    form = load_form()()

    if form.validate_on_submit():
        parse_form(form)

    return render_template('index.html', form=form)
