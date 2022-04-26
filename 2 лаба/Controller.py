import xml.sax
from typing import Any, List
from FullName import FullName

from FindByNameTur import FindStudentByNameOfTur
from FindBySport import FindStudentBySport
from FindByWinningSize import FindStudentByWinningSize
from DeliteByNumber import DeleteByNumber
from FindByNameTur import FindStudentIdByNameTur
from FindBySport import FindStudentIdBySport
from FindByWinningSize import FindStudentIdByWinningSize
from SaxParser import TurHandler
from TableMaker import TableMaker
from Table import Table


class StudentControllerImpl():

    def __init__(self):
        pass

    def print_all(self) -> List[Table]:
        handler = TurHandler()

        self._open_sax_parser_connection(handler)

        return TableMaker.table_creator(TurHandler.students)

    def find_student_by_name_tur(self, group_number: str) -> List[FullName]:

        handler = FindStudentByNameOfTur(group_number)

        self._open_sax_parser_connection(handler)

        return TableMaker.student_table_creator(handler.students)

    def find_student_by_sport(self, sport: str) -> List[Table]:
        handler = FindStudentBySport(sport)

        self._open_sax_parser_connection(handler)

        return TableMaker.student_table_creator(FindStudentBySport.students)

    def find_student_by_winning_size(self, size: str) -> List[Table]:
        handler = FindStudentByWinningSize(size)

        self._open_sax_parser_connection(handler)

        return TableMaker.student_table_creator(FindStudentByWinningSize.students)


    def delete_student_by_name_tur(self, name_tur: str) -> List[bool]:
        handler = FindStudentIdByNameTur(name_tur)

        self._open_sax_parser_connection(handler)

        bools: List[bool] = []
        for student_id in handler.get_student_id():
            dom_handler = DeleteByNumber(student_id)
            bools.append(dom_handler.delete_student_by_student_id())

        return TableMaker.bool_table_creator(bools)

    def delete_student_by_sport(self, sport: str) -> List[bool]:
        handler = FindStudentIdBySport(sport)

        self._open_sax_parser_connection(handler)

        bools: List[bool] = []
        for student_id in handler.get_student_id():
            dom_handler = DeleteByNumber(student_id)
            bools.append(dom_handler.delete_student_by_student_id())

        return TableMaker.bool_table_creator(bools)

    def delete_student_by_winning_size(self, size: str) -> List[bool]:
        handler = FindStudentIdByWinningSize(size)

        self._open_sax_parser_connection(handler)

        bools: List[bool] = []
        for student_id in handler.get_student_id():
            dom_handler = DeleteByNumber(student_id)
            bools.append(dom_handler.delete_student_by_student_id())

        return TableMaker.bool_table_creator(bools)

    @staticmethod
    def _open_sax_parser_connection(handler: Any):
        parser = xml.sax.make_parser()

        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        parser.setContentHandler(handler)

        parser.parse("DataTable.xml")
