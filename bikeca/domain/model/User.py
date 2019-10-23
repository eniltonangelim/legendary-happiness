class User:

    def __init__(self, user_type, gender, birth_year):
        self.__type = user_type
        self.__gender = gender
        self.__birthYear = birth_year

    def getgender(self):
        return self.__gender

    def gettype(self):
        return self.__type

    def getbirthyear(self):
        return self.__birthYear
