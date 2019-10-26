from bikeca.domain.model.trip import Trip
from bikeca.domain.port.usecases.trip import TripUsecase
from bikeca.domain.port.repository.trip import TripRepository
from typing import List


class FindTrips(TripUsecase):

    def __init__(self, repository: TripRepository):
        self._repository = repository

    def reader(self) -> List[Trip]:
        return self._repository.find_all()

