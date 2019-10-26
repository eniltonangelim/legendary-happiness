from bikeca.domain.port.repository.trip import TripRepository
from bikeca.domain.model.trip import Trip
from bikeca.domain.model.station import Station
from bikeca.domain.model.user import User
from typing import List
import csv


class TripRepositoryImpl(TripRepository):

    _raw = '/home/angelim/PycharmProjects/clean-architecture/data/raw/chicago.csv'

    def find_all(self) -> List[Trip]:
        _trips: List[Trip] = list()
        with open(self._raw, "r") as file_read:
            for row in csv.reader(file_read):
                trip: Trip = Trip()
                trip.start_time = row[0]
                trip.end_time = row[1]
                trip.duration = row[2]
                trip.start_station = Station(row[3])
                trip.end_station = Station(row[4])
                trip.user = User(row[5], row[6], row[7])
                _trips.append(trip)

        return _trips[1:]
