import os
import logging
import traceback

from http import HTTPStatus
from flask import Flask, jsonify, send_from_directory
from flask_injector import FlaskInjector, singleton
from werkzeug.exceptions import BadRequest


from app_people.api import api
from app_people.tinydb_storage import TinyDbStorage
from app_people.idata_storage import IDataStorage, PersonNotFoundError
from app_people.person_service import PersonService


def configure_dependencies(binder):
    binder.bind(interface=IDataStorage, to=TinyDbStorage, scope=singleton)
    binder.bind(PersonService, to=PersonService, scope=singleton)


def create_error(status_code, e):
    logging.error(e)
    traceback.print_tb(e.__traceback__)
    response = jsonify({'error': str(e)})
    response.status_code = status_code
    return response


def configure_single_page_app(app):
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        # only used for local build without nginx
        if path == "" or not os.path.exists('ui-people/build/' + path):
            return send_from_directory('ui-people/build', 'index.html')
        else:
            return send_from_directory('ui-people/build', path)


def setup_app():
    logging.basicConfig(level=logging.INFO)
    app = Flask('Python-React People app', static_folder='/ui-people/build')
    app.register_blueprint(api)
    configure_single_page_app(app)

    FlaskInjector(app=app, modules=[configure_dependencies])

    @app.errorhandler(BadRequest)
    def handle_400(e):
        return create_error(HTTPStatus.BAD_REQUEST, e)

    @app.errorhandler(PersonNotFoundError)
    def handle_404(e):
        return create_error(HTTPStatus.NOT_FOUND, e)

    @app.errorhandler(Exception)
    def handle_errors(e):
        return create_error(HTTPStatus.INTERNAL_SERVER_ERROR, e)
    return app


if __name__ == "__main__":
    flask_app = setup_app()
    flask_app.run(port=80)
