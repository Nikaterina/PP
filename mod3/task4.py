# Задача 4. Доверяй, но проверяй.
import unittest
from person import Person


class TestTrustFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.Person = Person("Екатерина", 1994, "Екатеринбург")

    def test_get_name(self):
        try:
            value = self.Person.__name
        except Exception as exp:
            self.assertRaises(type(exp))

    def test_get_address(self):
        try:
            value = self.Person.__address
        except Exception as exp:
            self.assertRaises(type(exp))

    def test_correct_get_age(self):
        self.assertTrue(self.Person.get_age() > 0)

    def test_set_name(self):
        try:
            self.Person.name = "Александр"
        except Exception as exp:
            self.assertRaises(type(exp))

    def test_set_address(self):
        try:
            self.Person.address = "Новосибирск"
        except Exception as exp:
            self.assertRaises(type(exp))

    def test_set_age(self):
        try:
            self.Person.age = 35
        except Exception as exp:
            self.assertRaises(type(exp))

    def address_is_not_none(self):
        self.assertTrue(self.Person.get_address() is not None)