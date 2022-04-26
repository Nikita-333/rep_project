import copy
import logging
import xml.sax
from typing import List

from Table import Table
from FullName import FullName


class FindStudentByNameOfTur(xml.sax.ContentHandler):
    students: List[FullName] = []

    def __init__(self, name_tur: str):
        self._current_data = ""
        self._surname = ""
        self._student_number = ""
        self._name = ""
        self._succession = ""
        #self.Table = Table()
        self._name_tur = name_tur
        self._is_expected = False
        self._table = FullName()

    def startElement(self, tag, attributes):
        self._current_data = tag

        if tag == "nameTur" and attributes["nameTur"] == self._name_tur:
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
                student_copy = copy.copy(self._table)
                FindStudentByNameOfTur.students.append(student_copy)

                self._is_expected = False
                self._current_data = ""

    def characters(self, content):
        if self._current_data == "surname":
            self._surname = content

        elif self._current_data == "name":
            self._name = content
        elif self._current_data == "succession":
            self._succession = content

    def get_name_tur(self):
        return self._name_tur

    def get_number(self):
        return list(self._student_number)



class FindStudentIdByNameTur(xml.sax.ContentHandler):
    student_id: int = 0

    def __init__(self, name_tur: str):
        self._current_data = ""
        self._students_group = {}
        self._group_number = name_tur

    def startElement(self, tag, attributes):
        self._current_data = tag

        if tag == "player":
            FindStudentIdByNameTur.student_id = int(attributes["number"])

        if tag == "nameTur" and attributes["nameTur"] == self._group_number:
            self._students_group[FindStudentIdByNameTur.student_id] = {self._group_number}

    def endElement(self, tag):
        pass

    def characters(self, content):
        pass

    def get_student_id(self):
        return list(self._students_group)
