from bikeca.domain.model.Station import Station
from bikeca.domain.model.User import User


class Trip:

    def __init__(self, start_at, end_at, duration, start_station: Station, end_station: Station, user: User):
        self.__startAt = start_at
        self.__endAt = end_at
        self.__duration = duration
        self.__startStation = start_station
        self.__endStation = end_station
        self.__user = user
