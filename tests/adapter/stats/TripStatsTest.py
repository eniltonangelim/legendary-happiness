from bikeca.domain.port.repository.trip import TripRepository
from bikeca.domain.port.usecases.stats import Stats
from bikeca.domain.model.gender import Gender
from bikeca.domain.model.types import Types
from bikeca.adapter.repository.trip_repository_impl import TripRepositoryImpl
from bikeca.adapter.stats.trip_stats_impl import TripStatsImpl
from bikeca.domain.model.trip import Trip
from typing import List
import unittest


class TripStatsTest(unittest.TestCase):

    _repository: TripRepository = TripRepositoryImpl()
    _stats: Stats = TripStatsImpl()
    _trips: List[Trip] = _repository.find_all()

    def test_trip_stats_instance(self):
        self.assertIsInstance(self._stats, Stats)

    def test_trip_only_gender(self):
        self.assertEqual(len(self._stats.only_gender(self._trips)), 1551505)

    def test_trip_count_gender(self):
        male, female = self._stats.count_gender(self._stats.only_gender(self._trips))
        self.assertEqual(male, 935854)
        self.assertEqual(female, 298784)

    def test_trip_most_popular_gender(self):
        male, female = self._stats.count_gender(self._stats.only_gender(self._trips))
        gender: Gender = self._stats.most_popular_gender(male, female)
        self.assertEqual(gender, Gender.MASCULINO)

    def test_trip_most_popular_user_types(self):
        customer, subscriber = self._stats.count_user_types(self._stats.only_user_types(self._trips))
        user_type: Types = self._stats.most_popular_user_types(customer, subscriber)
        self.assertEqual(user_type, Types.SUBSCRIBER)

    def test_trip_stats_min(self):
        min_trip: float = self._stats.min_trip(self._stats.only_duration(self._trips))
        self.assertEqual(round(min_trip), 60)

    def test_trip_stats_max(self):
        max_trip: float = self._stats.max_trip(self._stats.only_duration(self._trips))
        self.assertEqual(round(max_trip), 86338)

    def test_trip_stats_mean_duration(self):
        mean_trip: float = self._stats.mean_trip_duration(self._stats.only_duration(self._trips))
        self.assertEqual(round(mean_trip), 940)

    def test_trip_stats_median_duration(self):
        median_trip: float = self._stats.median_trip_duration(self._stats.only_duration(self._trips))
        self.assertEqual(round(median_trip), 670)


if __name__ == '__main__':
    unittest.main()