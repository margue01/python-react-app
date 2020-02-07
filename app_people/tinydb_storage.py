import uuid

from tinydb import TinyDB, Query

from app_people.idata_storage import IDataStorage, PersonNotFoundError


class TinyDbStorage(IDataStorage):

    def __init__(self):
        self.db = TinyDB('data/people.json')
        self.query = Query()

    def insert_person(self, name, age, balance, email, address):
        self.db.insert({
            'name': name,
            'age': age,
            'balance': balance,
            'email': email,
            'address': address,
            'flag': False,
            'person_id': str(uuid.uuid4())[:8]
        })

    def list_people(self):
        all_people = self.db.all()
        return all_people

    def delete_person(self, person_id):
        try:
            self.db.remove(self.query.person_id == person_id)
        except KeyError:
            raise PersonNotFoundError(f'Cannot find person {person_id}')

    def update_flag(self, person_id, enable):
        self.db.update({'flag': enable}, Query().person_id == person_id)

    def close(self):
        pass
