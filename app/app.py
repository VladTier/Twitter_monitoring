from flask import Flask
from extensions import db, migrate
from views import page_view
import config



def create_app():
    app = Flask(__name__)
    app.config.from_object(config.BaseConfig)
    print app.config
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(page_view)
    return app


