class Data:
    def __init__(self):
        self.__day: str = ""
        self.__month: str = ""
        self.__year: str = ""

    def get_data(self) -> str:
        dmy = (self.__day + "." + self.__month + "." + self.__year)

        return dmy

    def set_day(self, day):
        self.__day = day

    def set_month(self, month):
        self.__month = month

    def set_year(self, year):
        self.__year = year

    def get_day(self):
        return self.__day

    def get_month(self):
        return self.__month

    def get_year(self):
        return self.__year