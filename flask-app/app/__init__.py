from flask import Flask
from app.routes.routes import audio_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.register_blueprint(audio_routes)

    return app

if __name__ == '__main__':
    app = create_app()