from abc import ABC, abstractmethod


class PersonNotFoundError(Exception):
    pass


class IDataStorage(ABC):

    @abstractmethod
    def insert_person(self, name, age, balance, email, address):
        pass

    @abstractmethod
    def list_people(self):
        pass

    @abstractmethod
    def delete_person(self, person_id):
        pass

    @abstractmethod
    def close(self):
        pass
