from abc import ABC, abstractmethod

from app_people.person import Person


class PersonNotFoundError(Exception):
    pass


class IDataStorage(ABC):

    @abstractmethod
    def insert_person(self, person: Person):
        pass

    @abstractmethod
    def list_people(self, sort_by_key, limit):
        pass

    @abstractmethod
    def search_by_name(self, name):
        pass

    @abstractmethod
    def delete_person(self, person_id):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def update_flag(self, person_id, update_body):
        pass
