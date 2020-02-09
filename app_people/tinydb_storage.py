import re

from tinydb import TinyDB, Query

from app_people.idata_storage import IDataStorage, PersonNotFoundError
from app_people.person import Person, Field


class TinyDbStorage(IDataStorage):

    def __init__(self):
        self.db = TinyDB('data/people.json')
        self.query = Query()

    def insert_person(self, person: Person):
        self.db.insert({
            Field.NAME: person.name,
            Field.AGE: person.age,
            Field.BALANCE: person.balance,
            Field.EMAIL: person.email,
            Field.ADDRESS: person.address,
            Field.FLAG: person.flag,
            Field.PERSON_ID: person.person_id
        })

    def list_people(self, sort_by_key=None, limit=None):
        people = self.db.all()
        if sort_by_key:
            people.sort(key=lambda item: item[sort_by_key])
        return people[:limit]

    def search_by_name(self, name):
        return self.db.search(self.query.name.search(name, flags=re.IGNORECASE))

    def delete_person(self, person_id):
        try:
            self.db.remove(self.query.person_id == person_id)
        except KeyError:
            raise PersonNotFoundError(f'Cannot find person {person_id}')

    def update_flag(self, person_id, enable):
        self.db.update({Field.FLAG: enable}, Query().person_id == person_id)

    def close(self):
        self.db.close()
