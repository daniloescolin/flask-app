from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    
    # Load configuration from environment variables
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
    app.config['APP_NAME'] = os.getenv('APP_NAME', 'Flask GKE App')
    
    from .routes import main
    app.register_blueprint(main)
    
    return app