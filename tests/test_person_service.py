from unittest import TestCase
from unittest.mock import patch

from app_people.person_service import PersonService
from app_people.tinydb_storage import TinyDbStorage



MOCK_PEOPLE = [{'name': 'a'}, {'name': 'b'}]

class TestPersonService(TestCase):

    @patch('app_people.tinydb_storage.TinyDbStorage.list_people', return_value=MOCK_PEOPLE)
    def test_get_user(self, mock_get_person):
        person_service = PersonService(storage=TinyDbStorage())
        people = person_service.list_people()
        self.assertEqual(people, MOCK_PEOPLE)
