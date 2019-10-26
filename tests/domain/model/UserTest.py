import unittest
from bikeca.domain.model.user import User


class UserTest(unittest.TestCase):

    _user: User = User('Customer', 'Male', 1989.0)

    def test_user_instance(self):
        self.assertIsInstance(self._user, User)

    def test_user_birth_year(self):
        self.assertEqual(self._user.birth_year, 1989.0)

    def test_user_type(self):
        self.assertEqual(self._user.type, 'Customer')

    def test_user_gender(self):
        self.assertEqual(self._user.gender, 'Male')


if __name__ == '__main__':
    unittest.main()
