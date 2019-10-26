from typing import List, Tuple

from bikeca.domain.model.gender import Gender
from bikeca.domain.model.trip import Trip
from bikeca.domain.model.types import Types

from bikeca.domain.port.usecases.stats import Stats


class TripStatsImpl(Stats):

    def __init__(self):
        self._cast_to_float = lambda x: list(map(float, x))

    def only_gender(self, trips: List[Trip]) -> List[str]:
        return [trip.user.gender for trip in trips]

    def only_user_types(self, trips: List[Trip]) -> List[str]:
        return [trip.user.type for trip in trips]

    def only_duration(self, trips: List[Trip]) -> List[float]:
        return self._cast_to_float([trip.duration for trip in trips])

    def count_gender(self, genders: List[str]) -> Tuple[int, int]:
        male: int = len([gender for gender in genders if gender == 'Male'])
        female: int = len([gender for gender in genders if gender == 'Female'])
        return male, female

    def count_user_types(self, types: List[str]) -> Tuple[int, int]:
        customer: int = len([user_type for user_type in types if user_type == 'Customer'])
        subscriber: int = len([user_type for user_type in types if user_type == 'Subscriber'])
        return customer, subscriber

    def most_popular_gender(self, male: int, female: int) -> Gender:
        if male > female:
            answer = Gender.MASCULINO
        elif female > male:
            answer = Gender.FEMININO
        return answer

    def most_popular_user_types(self, customer: int, subscriber: int) -> Types:
        if customer > subscriber:
            answer = Types.CUSTOMER
        else:
            answer = Types.SUBSCRIBER
        return answer

    def max_trip(self, trips: List[float]) -> float:
        trips.sort()
        return trips[-1]

    def min_trip(self, trips: List[float]) -> float:
        trips.sort()
        return trips[0]

    def mean_trip_duration(self, trips: List[float]) -> float:
        trips.sort()
        return sum(trips) / len(trips)

    def median_trip_duration(self, trips: List[float]) -> float:
        trips.sort()
        length = len(trips)
        if length % 2 == 0:
            left_side = int(length / 2 - 1)
            right_side = int(length / 2)
            median_trip = float((int(trips[left_side]) + int(trips[right_side])) / 2)
        else:
            middle = int(length / 2)
            median_trip = float(trips[middle])
        return median_trip
