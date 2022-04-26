class FullName:
    def __init__(self):
        self.__surname: str = ""
        self.__name: str = ""
        self.__succession: str = ""

    def get_full_name(self) -> str:
        sns = self.__surname + " " + self.__name + " " + self.__succession
        return sns

    def set_surname(self, surname):
        self.__surname = surname

    def set_name(self, name):
        self.__name = name

    def set_succession(self, succession):
        self.__succession = succession

    def get_surname(self):
        return self.__surname

    def get_name(self):
        return self.__name

    def get_succession(self):
        return self.__succession

