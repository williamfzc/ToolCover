from flask import Blueprint


core_blueprint = Blueprint('core', __name__)

from . import views
