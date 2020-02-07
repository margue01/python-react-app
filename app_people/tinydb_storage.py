import uuid

from tinydb import TinyDB, Query

from app_people.idata_storage import IDataStorage, PersonNotFoundError
from app_people.person import Person


class TinyDbStorage(IDataStorage):

    def __init__(self):
        self.db = TinyDB('data/people.json')
        self.query = Query()

    def insert_person(self, person: Person):
        self.db.insert({
            'name': person.name,
            'age': person.age,
            'balance': person.balance,
            'email': person.email,
            'address': person.address,
            'flag': person.flag,
            'person_id': person.person_id
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


# if __name__ == "__main__":
#     storage = TinyDbStorage()
#     storage.insert_person(
#         name='Martin',
#         age=32,
#         balance=10.0,
#         email='m@g.com',
#         address='Dublin'
#     )
#     print(storage.db.search(Query().person_id == 'd61429ef'))
#     storage.update_flag('d61429ef', False)
#     print(storage.db.search(Query().person_id == 'd61429ef'))
#     storage.close()
