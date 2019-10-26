from abc import ABCMeta, abstractmethod
from bikeca.domain.model.trip import Trip
from typing import List


class TripUsecase(metaclass=ABCMeta):

    @abstractmethod
    def reader(self) -> List[Trip]:
        raise NotImplementedError("must define trip")
