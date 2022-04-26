import copy
import logging
import xml.sax
from typing import List

from FullName import FullName


class FindStudentBySport(xml.sax.ContentHandler):
    students: List[FullName] = []

    def __init__(self, sport: str):
        self._current_data = ""
        self._surname = ""
        self._student_number = ""
        self._name = ""
        self._succession = ""

        self._sport = sport
        self._is_expected = False
        self._table = FullName()

    def startElement(self, tag, attributes):
        self._current_data = tag

        if tag == "sport" and attributes["sport"] == self._sport:
            self._is_expected = True

        if tag == "player" and attributes["number"] == self._student_number:
            self._table.set_number(self._student_number)

    def endElement(self, tag):
        if self._is_expected is True:
            if self._current_data == "surname":
                self._table.set_surname(self._surname)
            elif self._current_data == "name":
                self._table.set_name(self._name)
            elif self._current_data == "succession":
                self._table.set_succession(self._succession)

                if self._table.get_name() == "":
                    logging.warning("Name field of id {} is empty!".format(self._student_number))
                elif self._table.get_surname() == "":
                    logging.warning("Surname field of id {} is empty!".format(self._student_number))
                elif self._table.get_succession() == "":
                    logging.warning("Succession field of id {} is empty!".format(self._student_number))

                student_copy = copy.copy(self._table)
                FindStudentBySport.students.append(student_copy)
                self._is_expected = False
                self._current_data = ""

    def characters(self, content):
        if self._current_data == "surname":
            self._surname = content
        elif self._current_data == "name":
            self._name = content
        elif self._current_data == "succession":
            self._succession = content

    def get_sport(self):
        return self._sport


class FindStudentIdBySport(xml.sax.ContentHandler):
    student_id: int = 0

    def __init__(self, sport: str):
        self._current_data = ""
        self._students_group = {}
        self._group_number = sport

    def startElement(self, tag, attributes):
        self._current_data = tag

        if tag == "player":
            FindStudentIdBySport.student_id = int(attributes["number"])

        if tag == "sport" and attributes["sport"] == self._group_number:
            self._students_group[FindStudentIdBySport.student_id] = {self._group_number}

    def endElement(self, tag):
        pass

    def characters(self, content):
        pass

    def get_student_id(self):
        return list(self._students_group)