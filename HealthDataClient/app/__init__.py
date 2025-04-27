from flask import Flask
from app.routes.healthdata import healthdata_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # ← load config here

    from app.routes.healthdata import healthdata_bp
    app.register_blueprint(healthdata_bp, url_prefix='/healthdata')

    return app
