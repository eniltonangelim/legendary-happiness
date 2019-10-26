import unittest
from bikeca.domain.model.trip import Trip
from bikeca.domain.model.user import User
from bikeca.domain.model.station import Station


class UserTest(unittest.TestCase):

    _trip: Trip = Trip('Beira Mar')

    def test_station_instance(self):
        self.assertIsInstance(self._trip, Trip)

    def test_station_user(self):
        _user: User = User('Customer', 'Female', 1989.0)
        self._trip.user = _user
        self.assertEqual(self._trip.user.gender, 'Female')

    def test_station_station(self):
        _station: Station = Station('Beira Mar CLT')
        self._trip.station = _station
        self.assertEqual(self._trip.station.name, 'Beira Mar CLT')


if __name__ == '__main__':
    unittest.main()