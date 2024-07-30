from flask import Flask
from app.apis.notification_blueprint import notifications_blueprint
from app.apis.admin_blueprint import admin_blueprint

def get_flask_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(admin_blueprint)
    flask_app.register_blueprint(notifications_blueprint)

    return flask_app