import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):

    def test_city_country(self):
        formatted_city_country = city_country('Seoul', 'South Korea')
        self.assertEqual(formatted_city_country, 'Seoul, South Korea - ')

if __name__ == '__main__':
    unittest.main()

