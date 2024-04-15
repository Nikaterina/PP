# Задача 1. Хорошего дня!
import unittest
from freezegun import freeze_time
from mod2.task4 import app


class TestCorrectWeekday(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    @freeze_time("2024-04-05")
    def test_correct_weekday(self):
        username = "Katya"
        greeting = "Хорошей пятницы!"
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(greeting in response_text)