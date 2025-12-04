from flask import Blueprint
from controllers.user_controller import register_user, login_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def route_register():
    return register_user()

@user_bp.route('/login', methods=['POST'])
def route_login():
    return login_user()