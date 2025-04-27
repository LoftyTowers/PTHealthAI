from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.healthdata import healthdata_bp
    app.register_blueprint(healthdata_bp, url_prefix='/healthdata')

    return app
