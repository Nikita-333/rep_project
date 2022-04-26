import copy
import logging
import xml.sax
from typing import List

from FullName import FullName



class FindStudentByWinningSize(xml.sax.ContentHandler):
    students: List[FullName] = []

    def __init__(self, size: str):
        self._current_data = ""
        self._surname = ""
        self._student_number = ""
        self._name = ""
        self._succession = ""

        self._size = size
        self._winning_size_float = int(self._size)/0.6
        self._winning_size = str(self._winning_size_float)
        self._is_expected = False
        self._table = FullName()

    def startElement(self, tag, attributes):
        self._current_data = tag

        if tag == "winningSize" and attributes["winningSize"] == self._winning_size:
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
                FindStudentByWinningSize.students.append(student_copy)
                self._is_expected = False
                self._current_data = ""

    def characters(self, content):
        if self._current_data == "surname":
            self._surname = content
        elif self._current_data == "name":
            self._name = content
        elif self._current_data == "succession":
            self._succession = content

    def get_winning_size(self):
        return self._winning_size


class FindStudentIdByWinningSize(xml.sax.ContentHandler):
    student_id: int = 0

    def __init__(self, size: str):
        self._current_data = ""
        self._students_group = {}
        self._group_number = str(int(size)/0.6)

    def startElement(self, tag, attributes):
        self._current_data = tag

        if tag == "player":
            FindStudentIdByWinningSize.student_id = int(attributes["number"])

        if tag == "winningSize" and attributes["winningSize"] == self._group_number:
            self._students_group[FindStudentIdByWinningSize.student_id] = {self._group_number}

    def endElement(self, tag):
        pass

    def characters(self, content):
        pass

    def get_student_id(self):
        return list(self._students_group)