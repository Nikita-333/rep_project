from Data import Data
from FullName import FullName

class Table:
     def __init__(self):
         self.__name_tournament: str = ""
         self.data = Data()
         self.__types_sports: str = ""
         self.full_name = FullName()
         self.__winning_size: str = ""
         self.__earning_winnings: str = ""
         self.__number = ""
         self.__name: str =""
         self.__data: str = ""

     def get_name_tour(self):
         return self.__name_tournament

     def get_types_sport(self):
         return self.__types_sports

     def get_winning_size(self):
         return self.__winning_size

     def get_earning_winning(self):
         return self.__earning_winnings

     def set_name_tour(self, name):
         self.__name_tournament = name

     def set_types_sport(self, sport):
         self.__types_sports = sport

     def set_winning_size(self, winning):
         self.__winning_size = winning

     def get_earning_winning(self):
         self.__earning_winnings_float =float(self.__winning_size) * 0.6
         self.__earning_winnings = str(self.__earning_winnings_float)
         return self.__earning_winnings

     def set_number(self, number):
         self.__number = number

     def get_number(self):
         return self.__number

     def set_name(self, name):
         self.__name=name

     def get_name(self):
        return self.__name

     def set_data(self, data):
         self.data = data

     def get_data(self):
        return self.data
     ##def get_name(self):
      ##   return self.__full_name

