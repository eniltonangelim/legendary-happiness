import unittest
from bikeca.domain.model.station import Station


class UserTest(unittest.TestCase):

    _station: Station = Station('Beira Mar')

    def test_station_instance(self):
        self.assertIsInstance(self._station, Station)

    def test_station_name(self):
        self.assertEqual(self._station.name, 'Beira Mar')


if __name__ == '__main__':
    unittest.main()
