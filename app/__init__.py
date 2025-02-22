from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes import api
    app.register_blueprint(api)

    @app.route('/')
    def index():
        return send_from_directory('static', 'index.html')

    with app.app_context():
        db.create_all()

    return app