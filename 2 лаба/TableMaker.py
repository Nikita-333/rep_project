from typing import List

from tabulate import tabulate

from FullName import FullName
from Table import Table
import copy

class TableMaker:

    @staticmethod
    def student_table_creator(students: List[FullName]):
        head = ["name", "surname", "succession"]
        studs: list = []
        s: list = []
        for i in students:
            s.append(i.get_name())
            s.append(i.get_surname())
            s.append(i.get_succession())
            a = copy.copy(s)
            studs.append(a)
            s.clear()

        return tabulate(studs, headers=head, tablefmt="grid", stralign="center")

    def table_creator(students: List[Table]):
        head = ["name of tur", "data", "sport", "SNS", "winning size", "earning_winning"]
        studs: list = []
        s: list = []
        for i in students:
            s.append(i.get_name_tour())
            s.append(i.get_data())
            s.append(i.get_types_sport())
            s.append(i.get_name())
            s.append(i.get_winning_size())
            s.append(i.get_earning_winning())
            a = copy.copy(s)
            studs.append(a)
            s.clear()


        return tabulate(studs, headers=head, tablefmt="grid", stralign="center")

    @staticmethod
    def bool_table_creator(bools: List[bool]):
        head = ["is deleted"]
        is_deleted: list = []
        s: list = []
        for i in bools:
            s.append(i)
            a = copy.copy(s)
            is_deleted.append(a)
            s.clear()

        return tabulate(is_deleted, headers=head, tablefmt="grid", stralign="center")



