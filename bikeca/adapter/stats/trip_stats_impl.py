from typing import List, Tuple

from bikeca.domain.model.gender import Gender
from bikeca.domain.model.trip import Trip
from bikeca.domain.model.types import Types

from bikeca.domain.port.usecases.stats import Stats


class TripStatsImpl(Stats):

    def __init__(self):
        self._cast_to_float = lambda x: list(map(float, x))

    def only_gender(self, trips: List[Trip]) -> List[str]:
        pass

    def only_user_types(self, trips: List[Trip]) -> List[str]:
        pass

    def only_duration(self, trips: List[Trip]) -> List[float]:
        return self._cast_to_float([trip.duration for trip in trips])

    def count_gender(self, trips: List[Trip]) -> Tuple[int, int]:
        pass

    def count_user_types(self, trips: List[Trip]) -> Tuple[int, int]:
        pass

    def most_popular_gender(self, trips: List[Trip]) -> Gender:
        pass

    def most_popular_user_types(self, trips: List[Trip]) -> Types:
        pass

    def max_trip(self, trips: List[float]) -> float:
        pass

    def min_trip(self, trips: List[float]) -> float:
        trips.sort()
        return trips[0]

    def mean_trip_duration(self, trips: List[float]) -> float:
        pass

    def median_trip_duration(self, trips: List[float]) -> float:
        pass

