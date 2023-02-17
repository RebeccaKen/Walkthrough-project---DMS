import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa
from .database import db

def create_app():
    app = Flask('taskmanager')
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    if os.environ.get("DEVELOPMENT") == "True":
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
    else:
        uri = os.environ.get("DB_URL")
        if uri.startswith("postgres://"):
            uri = uri.replace("postgres://", "postgresql://", 1)
        app.config["SQLALCHEMY_DATABASE_URI"] = uri

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


app = create_app()

from taskmanager import routes  # noqa
