from abc import ABCMeta, abstractmethod
from typing import List
from bikeca.domain.model.trip import Trip


class TripRepository(metaclass=ABCMeta):

    @abstractmethod
    def find_all(self) -> List[Trip]:
        raise NotImplementedError("must define find all")
