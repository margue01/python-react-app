import uuid


class Field:
    NAME = 'name'
    AGE = 'age'
    EMAIL = 'email'
    BALANCE = 'balance'
    ADDRESS = 'address'
    PERSON_ID = 'person_id'
    FLAG = 'flag'


class Person:

    def __init__(self, name, age, balance, email, address, flag=False, person_id=None):
        self._name = name
        self._age = age
        self._balance = balance
        self._email = email
        self._address = address
        self._flag = flag
        self._person_id = person_id if person_id else str(uuid.uuid4())[:8]

    def as_dict(self):
        return {
            Field.NAME: self._name,
            Field.AGE: self._age,
            Field.BALANCE: self._balance,
            Field.EMAIL: self._email,
            Field.ADDRESS: self._address,
            Field.FLAG: self._flag,
            Field.PERSON_ID: self._person_id
        }

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def email(self):
        return self._email

    @property
    def balance(self):
        return self._balance

    @property
    def address(self):
        return self._address

    @property
    def flag(self):
        return self._flag

    @property
    def person_id(self):
        return self._person_id
