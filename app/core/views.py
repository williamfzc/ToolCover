from ..core import core_blueprint
from flask import render_template


@core_blueprint.route('/')
def index():
    return render_template('index.html')
