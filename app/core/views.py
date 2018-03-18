from ..core import core_blueprint
from flask import render_template
from .runner import sub_app


@core_blueprint.route('/')
def index():
    # 当回到主页时需要reset所有状态
    sub_output = sub_app.stdout.readline()
    return render_template('index.html', content=sub_output)
