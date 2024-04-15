# Задача 2. Дешифратор.
import unittest
from mod2.task3 import decrypt


class TestCorrectDecryption(unittest.TestCase):
    def test_correct_decr_OPs(self):
        self.assertEqual(decrypt('абра-кадабра.'), 'абра-кадабра')
        self.assertEqual(decrypt('.'), '')

    def test_correct_decr_TPs(self):
        self.assertEqual(decrypt('абраа..-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абра--..кадабра'), 'абра-кадабра')

    def test_correct_decr_MPs(self):
        self.assertEqual(decrypt('абраа..-.кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абрау...-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абра........'), '')
        self.assertEqual(decrypt('абр......а.'), 'а')
        self.assertEqual(decrypt('1..2.3'), '23')
        self.assertEqual(decrypt('1.......................'), '')