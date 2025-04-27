from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # ← load config here

    from app.routes.users import users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    return app
