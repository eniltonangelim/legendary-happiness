class User:

    def __init__(self, user_type=None, gender=None, birth_year=None):
        self._type = user_type
        self._gender = gender
        self._birth_year = birth_year

    @property
    def birth_year(self) -> str:
        return self._birth_year

    @property
    def gender(self) -> str:
        return self._gender

    @property
    def type(self) -> str:
        return self._type

    @birth_year.setter
    def birth_year(self, birth_year):
        self._birth_year = birth_year

    @birth_year.deleter
    def birth_year(self):
        del self._birth_year

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    @gender.deleter
    def gender(self):
        del self._gender

    @type.setter
    def type(self, user_type):
        self._type = user_type

    @type.deleter
    def type(self):
        del self._type
