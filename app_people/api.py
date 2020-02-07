from http import HTTPStatus
from flask import Blueprint, jsonify, request
from flask_injector import inject
from werkzeug.exceptions import BadRequest

from app_people import __version__
from app_people.person_service import PersonService

API_BASE = '/app/people'
ENDPOINT_HEALTHCHECK = f'/app/healthcheck'
ENDPOINT_VERSION = f'/app/version'
CONTENT_TYPE = 'Content-Type'
CONTENT_TYPE_JSON = 'application/json'


api = Blueprint('base', __name__)


def check_json_type(headers):
    if CONTENT_TYPE not in headers or CONTENT_TYPE_JSON not in headers[CONTENT_TYPE]:
        raise BadRequest(description=f'Expected request with Content-Type of "{CONTENT_TYPE_JSON}"')


@api.route(f'{ENDPOINT_HEALTHCHECK}', methods=['GET'])
def healthcheck():
    return jsonify({'status': 'ok'}), HTTPStatus.OK


@api.route(f'{ENDPOINT_VERSION}', methods=['GET'])
def version():
    return jsonify({'version': __version__}), HTTPStatus.OK


@inject
@api.route(f'{API_BASE}', methods=['GET'])
def list_people(person_service: PersonService):
    people = person_service.list_people()
    return jsonify(people), HTTPStatus.OK


@inject
@api.route(f'{API_BASE}', methods=['POST'])
def create_person(person_service: PersonService):
    check_json_type(request.headers)
    person_service.create_person(request.json)
    return jsonify({'created': 'ok'}), HTTPStatus.OK


@inject
@api.route(f'{API_BASE}/<person_id>', methods=['PUT'])
def update_person(person_id, person_service: PersonService):
    check_json_type(request.headers)
    person_service.update_person(person_id, request.json)
    return jsonify({'updated': 'ok'}), HTTPStatus.OK


@inject
@api.route(f'{API_BASE}/<person_id>', methods=['DELETE'])
def delete_person(person_id, person_service: PersonService):
    person_service.delete_person(person_id)
    return jsonify({'deleted': 'ok'}), HTTPStatus.OK
