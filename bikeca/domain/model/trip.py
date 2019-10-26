from bikeca.domain.model.station import Station
from bikeca.domain.model.user import User


class Trip:

    def __init__(self, start_time=None, end_time=None, duration=None, start_station: Station = Station(),
                 end_station: Station = Station(), user: User = User()):
        self._start_time = start_time
        self._end_time = end_time
        self._duration = duration
        self._start_station = start_station
        self._end_station = end_station
        self._user = user

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def duration(self):
        return self._duration

    @property
    def start_station(self) -> Station:
        return self._start_station

    @property
    def end_station(self) -> Station:
        return self._end_station

    @property
    def user(self) -> User:
        return self._user

    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time

    @end_time.setter
    def end_time(self, end_time):
        self._end_time = end_time

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @start_station.setter
    def start_station(self, start_station):
        self._start_station = start_station

    @end_station.setter
    def end_station(self, end_station):
        self._end_station = end_station

    @user.setter
    def user(self, user):
        self._user = user

