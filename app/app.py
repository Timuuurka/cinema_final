from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    INSTANCE_DIR = os.path.join(BASE_DIR, "..", "instance")

    os.makedirs(INSTANCE_DIR, exist_ok=True)

    app.config["SECRET_KEY"] = "cinema-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(INSTANCE_DIR, "cinema.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
