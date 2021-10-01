from flask import Blueprint
from flask import render_template

auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signin', methods=['GET'])
def signin():
    return render_template('signin.html')
