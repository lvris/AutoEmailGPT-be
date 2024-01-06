from flask import Flask
from services import config
from services import log
from services import run
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    config.route(app)
    log.route(app)
    run.route(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
