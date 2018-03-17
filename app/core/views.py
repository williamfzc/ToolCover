from ..core import core_blueprint
from flask import render_template


@core_blueprint.route('/')
def index():
    # 当回到主页时需要reset所有状态
    # TODO: 当前请求时会卡死 需要debug
    from .. import sub_app
    sub_output = sub_app.stdout.read()
    return render_template('index.html', content=sub_output)
