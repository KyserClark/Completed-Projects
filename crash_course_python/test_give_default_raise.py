import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.kyser = Employee('Kyser', 'Clark', 150_000)
        self.salary = 150_000

    def test_give_default_raise(self):
        self.kyser.give_raise()
        self.assertEqual(self.kyser.salary, 155_000)

    def test_give_custom_raise(self):
        self.kyser.give_raise(100_000)
        self.assertEqual(self.kyser.salary, 250_000)

    if __name__ == '__main__':
        unittest.main()
