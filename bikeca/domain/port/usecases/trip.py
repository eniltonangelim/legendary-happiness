from abc import ABCMeta, abstractmethod
from bikeca.domain.model.trip import Trip
from typing import List


class TripUsecase(metaclass=ABCMeta):

    @abstractmethod
    def reader(self) -> List[Trip]:
        raise NotImplementedError("must define trip")


class StatsTripUsecase(metaclass=ABCMeta):

    @abstractmethod
    def popular_gender(self):
        raise NotImplementedError("must define popular_gender")
