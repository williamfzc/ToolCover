"""
主要完成初始化

1. 应用初始化
2. 蓝图配置
"""
from flask import Flask
from flask_bootstrap import Bootstrap
from app.core.runner import get_app_process


bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)

    # 配置蓝图
    from app.core import core_blueprint
    app.register_blueprint(core_blueprint)

    # 启动子程序
    sub_app = get_app_process()
    globals()['sub_app'] = sub_app

    return app
