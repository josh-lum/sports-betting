from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# create db instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialize db with app context
    db.init_app(app)

    # register main blueprint for routes
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app