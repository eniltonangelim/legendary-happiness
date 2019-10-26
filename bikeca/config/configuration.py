from bikeca.adapter.repository.trip_repository_impl import TripRepositoryImpl
from bikeca.adapter.stats.trip_stats_impl import TripStatsImpl
from bikeca.domain.port.configuration.configurable import Configurable
from bikeca.domain.port.repository.trip import TripRepository
from bikeca.domain.port.usecases.trip import StatsTripUsecase
from bikeca.usecases.trip.stats_trip import StatsTrip


class Configuration(Configurable):

    def statistic(self) -> StatsTripUsecase:
        return StatsTrip(TripStatsImpl(), TripRepositoryImpl())

    def repository(self) -> TripRepository:
        pass