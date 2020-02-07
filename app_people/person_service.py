from flask_injector import inject

from app_people.idata_storage import IDataStorage


class Field:
    ENABLE = "enable"


class PersonService:

    @inject
    def __init__(self, storage: IDataStorage):
        self.storage = storage

    def create_person(self, person_body):
        self.storage.insert_person(
            name=person_body['name'],
            age=person_body['age'],
            email=person_body['email'],
            address=person_body['address'],
            balance=person_body['balance']
        )

    def delete_person(self, person_id):
        self.storage.delete_person(person_id=person_id)

    def list_people(self):
        return self.storage.list_people()

    def update_person(self, person_id, update_body):
        if Field.ENABLE in update_body:
            self.storage.update_flag(person_id, update_body[Field.ENABLE])
