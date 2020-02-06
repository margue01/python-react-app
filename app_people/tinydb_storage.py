import logging

from tinydb import TinyDB

from app_people.idata_storage import IDataStorage, PersonNotFoundError


class TinyDbStorage(IDataStorage):

    def __init__(self):
        self.db = TinyDB('data/people.json')

    def insert_person(self, name, age, balance, email, address):
        self.db.insert({
            'name': name,
            'age': age,
            'balance': balance,
            'email': email,
            'address': address,
            'flag': False,
        })

    def list_people(self):
        all_people = self.db.all()
        return [p.update({'doc_id': p.doc_id}) or p for p in all_people]

    def delete_person(self, person_id):
        doc_id = int(person_id)
        try:
            self.db.remove(doc_ids=[doc_id])
        except KeyError:
            raise PersonNotFoundError(f'Cannot find person {doc_id}')

    def close(self):
        pass
