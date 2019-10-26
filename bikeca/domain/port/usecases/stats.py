from abc import ABCMeta, abstractmethod
from typing import List, Tuple
from bikeca.domain.model.trip import Trip
from bikeca.domain.model.gender import Gender
from bikeca.domain.model.types import Types


class Stats(metaclass=ABCMeta):

    @abstractmethod
    def only_gender(self, trips: List[Trip]) -> List[str]:
        """
        Função para criar uma lista apartir do genero do conjunto de dados (data)
        Argumentos:
           data: Conjunto de dados usado para extrair a coluna (index)
        Retorna:
           Uma lista usando apenas uma coluna da amostra de dados
        """
        raise NotImplementedError("stats must define only_gender method")

    @abstractmethod
    def only_user_types(self, trips: List[Trip]) -> List[str]:
        """
        Função para criar uma lista apartir dos tipos de usuário do conjunto de dados (data)
        Argumentos:
           data: Conjunto de dados usado para extrair a coluna (index)
        Retorna:
           Uma lista usando apenas uma coluna da amostra de dados
        """
        raise NotImplementedError("stats must define only_user_type method")

    @abstractmethod
    def only_duration(self, trips: List[Trip]) -> List[float]:
        """
        Função para criar uma lista apartir da duração da viagem do conjunto de dados (data)
        Argumentos:
           data: Conjunto de dados usado para extrair a coluna (index)
        Retorna:
           Uma lista usando apenas uma coluna da amostra de dados
        """
        raise NotImplementedError("stats must define only_duration method")

    @abstractmethod
    def count_gender(self, genders: List[str]) -> Tuple[int, int]:
        """
        Função para contabilizar os gêneros do conjunto de dados
        Argumentos:
           data_list: Conjunto de dados
        Retorna:
           Uma lista com a quantidade de gênero Masculino e Feminino encontrados na amostra de dados
        """
        raise NotImplementedError("stats must define count_gender method")

    @abstractmethod
    def count_user_types(self, types: List[str]) -> Tuple[int, int]:
        """
        Função para contabilizar os tipos de usuário do conjunto de dados
        Argumentos:
           data_list: Conjunto de dados
        Retorna:
           Uma lista com a quantidade de gênero Masculino e Feminino encontrados na amostra de dados
        """
        raise NotImplementedError("stats must define count_user_types method")

    @abstractmethod
    def most_popular_gender(self, male: int, female: int) -> Gender:
        """
        Função para classificar o gênero mais popular no conjunto de dados
        Argumentos:
            data_list: Amostra de dados
        Retorna:
            Uma string com a classificação do genero mais popular.
        """
        raise NotImplementedError("stats must define most_popular_gender method")

    @abstractmethod
    def most_popular_user_types(self, customer: int, subscriber: int) -> Types:
        """
        Função para classificar o tipo de usuário mais popular no conjunto de dados
        Argumentos:
            data_list: Amostra de dados
        Retorna:
            Uma string com a classificação do genero mais popular.
        """
        raise NotImplementedError("stats must define most_popular_user_types method")

    @abstractmethod
    def max_trip(self, trips: List[float]) -> float:
        """
        Função para indicar o valor máximo de uma amostra de dados
        Argumentos:
            trip_duration_data: A lista contendo dados da viagem
        Retorna:
            O maior número float da amostra
        """
        raise NotImplementedError("stats must define count_user_types method")

    @abstractmethod
    def min_trip(self, trips: List[float]) -> float:
        """
        Função para indicar o valor minimo de uma amostra de dados
        Argumentos:
            trip_duration_data: A lista contendo dados da viagem
        Retorna:
            O menor número float da amostra
        """
        raise NotImplementedError("stats must define count_user_types method")

    @abstractmethod
    def mean_trip_duration(self, trips: List[float]) -> float:
        """
        Função para indicar o valor da média de uma amostra de dados
        Argumentos:
            trip_duration_data: A lista contendo dados da viagem
        Retorna:
            A média entre os valores da amostra
        """
        raise NotImplementedError("stats must define count_user_types method")

    @abstractmethod
    def median_trip_duration(self, trips: List[float]) -> float:
        """
        Função para indicar o valor central de uma amostra de dados
        Argumentos:
            trip_duration_data: A lista contendo dados da viagem
        Retorna:
            O valor central da amostra de dados
        """
        raise NotImplementedError("stats must define count_user_types method")
