import xml.sax
import logging
from Data import Data
from FullName import FullName
from Table import Table
from typing import List
import copy

class TurHandler(xml.sax.ContentHandler):
   students: List[Table] = []

   def __init__(self):
        self._current_data = ""
        self._student_number = ""
        self.Table = Table()
        self.Fullname = FullName()
        self.Data = Data()
        self._day: str = ""
        self._month: str = ""
        self._year: str = ""
        self._surname: str = ""
        self._name: str = ""
        self._succession: str = ""

   def startElement(self, tag, attributes):
      self._current_data = tag
      if tag == "nameTur":
         title = attributes["nameTur"]
         self.Table.set_name_tour(title)
      if tag == "sport":
         title = attributes["sport"]
         self.Table.set_types_sport(title)
      if tag == "winningSize":
         title = attributes["winningSize"]
         self.Table.set_winning_size(title)
      if tag == "player" and attributes["number"] == self._student_number:
          self.Table.set_number(self._student_number)


   def characters(self, content):
      if self._current_data == "day":
         self._day = content
      elif self._current_data == "month":
         self._month = content
      elif self._current_data == "year":
         self._year = content
      elif self._current_data == "surname":
         self._surname = content
      elif self._current_data == "name":
         self._name = content
      elif self._current_data == "succession":
         self._succession = content

   def endElement(self, tag):
      if self._current_data == "day":
         self.Data.set_day(self._day)
      elif self._current_data == "month":
         self.Data.set_month(self._month)
      elif self._current_data == "year":
         self.Data.set_year(self._year)
         self.Table.set_data(self.Data.get_data())
      elif self._current_data == "surname":
         self.Fullname.set_surname(self._surname)
      elif self._current_data == "name":
         self.Fullname.set_name(self._name)
      elif self._current_data == "succession":
         self.Fullname.set_succession(self._succession)
         self.Table.set_name(self.Fullname.get_full_name())
         if self.Fullname.get_name() == "":
             logging.warning("Name field of id {} is empty!".format(self._student_number))
         elif self.Fullname.get_surname() == "":
             logging.warning("Surname field of id {} is empty!".format(self._student_number))
         elif self.Fullname.get_succession() == "":
             logging.warning("Succession field of id {} is empty!".format(self._student_number))

         student_copy = copy.copy(self.Table)
         TurHandler.students.append(student_copy)
      self._current_data = ""










