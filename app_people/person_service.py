from flask_injector import inject

from app_people.idata_storage import IDataStorage
from app_people.person import Person


class Field:
    ENABLE = "enable"


class PersonService:

    @inject
    def __init__(self, storage: IDataStorage):
        self.storage = storage

    def create_person(self, person_body):
        person = Person(
            name=person_body['name'],
            age=person_body['age'],
            email=person_body['email'],
            address=person_body['address'],
            balance=person_body['balance']
        )
        self.storage.insert_person(person)

    def delete_person(self, person_id):
        self.storage.delete_person(person_id=person_id)

    def list_people(self, name=None, sort_by_key=None, limit=None):
        if name:
            people = self.storage.search_by_name(name)
        else:
            people = self.storage.list_people()
        if sort_by_key and self._is_valid_key(sort_by_key):
            people.sort(key=lambda item: item[sort_by_key])
        return people[:self._get_limit(limit)]

    def update_person(self, person_id, update_body):
        if Field.ENABLE in update_body:
            self.storage.update_flag(person_id, update_body[Field.ENABLE])

    @staticmethod
    def _is_valid_key(key):
        return key in ['name', 'email', 'age', 'balance']

    @staticmethod
    def _get_limit(limit):
        if limit:
            try:
                return int(limit)
            except ValueError:
                return None
        return limit
