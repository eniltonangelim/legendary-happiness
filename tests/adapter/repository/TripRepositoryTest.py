from bikeca.domain.port.repository.trip import TripRepository
from bikeca.adapter.repository.trip_repository_impl import TripRepositoryImpl
from bikeca.domain.model.trip import Trip
from typing import List
import unittest


class TripRepositoryTest(unittest.TestCase):

    _repository: TripRepository = TripRepositoryImpl()
    _trips: List[Trip] = _repository.find_all()

    def test_trip_instance(self):
        self.assertIsInstance(self._repository, TripRepository)

    def test_trip_list(self):
        self.assertEqual(len(self._trips[1:21]), 20)

    def test_trip_start_station(self):
        self.assertEqual(self._trips[1].start_station.name, 'Larrabee St & Menomonee St')


if __name__ == '__main__':
    unittest.main()