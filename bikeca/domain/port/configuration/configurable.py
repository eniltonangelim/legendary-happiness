from abc import ABCMeta, abstractmethod

from bikeca.domain.port.repository.trip import TripRepository
from bikeca.domain.port.usecases.trip import StatsTripUsecase


class Configurable(metaclass=ABCMeta):

    @abstractmethod
    def statistic(self) -> StatsTripUsecase:
        raise NotImplementedError("config must define statistic method")

    @abstractmethod
    def repository(self) -> TripRepository:
        raise NotImplementedError("config must define repository method")
