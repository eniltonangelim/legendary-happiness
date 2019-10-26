from typing import List

from bikeca.domain.model.gender import Gender
from bikeca.domain.model.trip import Trip
from bikeca.domain.port.repository.trip import TripRepository
from bikeca.domain.port.usecases.stats import Stats
from bikeca.domain.port.usecases.trip import StatsTripUsecase


class StatsTrip(StatsTripUsecase):

    def __init__(self, stats: Stats, repository: TripRepository):
        self._stats = stats
        self._repository = repository

    def popular_gender(self):
        trips: List[Trip] = self._repository.find_all()
        genders: List[str] = self._stats.only_gender(trips)
        male, female = self._stats.count_gender(genders)
        answer: Gender = self._stats.most_popular_gender(male, female)
        print("Genero mais popular: {0}".format(answer))
