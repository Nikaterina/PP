# Задача 3. Учёт финансов.
import unittest
from mod2.task7 import app


class TestAccountingOfFinances(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()

    def test_EP_add(self):
        user_date = ["20240105", "20240103", "20240209", "20230307"]
        summ = ['15000', '300', '45', '1']
        expected_summ = ['25600', '25900', '548', '1']
        for i in range(len(user_date)):
            url = "/add/" + user_date[i] + "/" + summ[i]
            response_data = self.app.get(url).data.decode()
            self.assertTrue(expected_summ[i] in response_data)

    def test_EP_calc_month(self):
        year = "2024"
        month = ['01', '02', '03']
        expected_summ = ['25900', '548', '0']
        for i in range(len(month)):
            url = "/calculate/" + year + "/" + month[i]
            response_data = self.app.get(url).data.decode()
            self.assertTrue(expected_summ[i] in response_data)

    def test_EP_calc_year(self):
        year = ['2024', '2023', '2000']
        expected_summ = ['26448', '1', '0']
        for i in range(len(year)):
            url = "/calculate/" + year[i]
            response_data = self.app.get(url).data.decode()
            self.assertTrue(expected_summ[i] in response_data)

    def test_invalid_data(self):
        date = "202405e2"
        summ = "800"
        url = "/add/" + date + "/" + summ
        try:
            self.app.get(url)
        except:
            self.assertRaises(ValueError)
