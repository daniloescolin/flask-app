from flask import Blueprint, render_template
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    app_name = os.getenv('APP_NAME', 'Flask GKE App')
    return render_template('index.html', app_name=app_name)