import unittest
from bikeca.domain.model.User import User


class UserTest(unittest.TestCase):

    __user: User = User('Customer', 'Male', 1989.0)

    def test_user_instance(self):
        self.assertIsInstance(self.__user, User)

    def test_user_birth_year(self):
        self.assertEqual(self.__user.getbirthyear(), 1989.0)

    def test_user_type(self):
        self.assertEqual(self.__user.gettype(), 'Customer')

    def test_user_gender(self):
        self.assertEqual(self.__user.getgender(), 'Male')


if __name__ == '__main__':
    unittest.main()
