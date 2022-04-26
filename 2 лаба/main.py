from Table import Table
import xml.sax
from SaxParser import TurHandler
from Controller import StudentControllerImpl
from FindByNameTur import FindStudentByNameOfTur
from FindBySport import FindStudentBySport
from FindByWinningSize import FindStudentByWinningSize
from SaxParser import TurHandler
from typing import List





StudentControllerImpl=StudentControllerImpl()

while True:

    ##Вывод всего
    print(StudentControllerImpl.print_all())
    TurHandler.students.clear()

    print("1 - search by name of tur\n"
          "2 - search by name of sport\n"
          "3 - search by earning winnings\n"
          "4 - delete by name of tur\n"
          "5 - delete by name of sport\n"
          "6 - delete by earning winnings\n"
          "7 - exit")

    choice = input()

    if choice == "1":
        print("type group number ")
        name_tur = input()
        print(StudentControllerImpl.find_student_by_name_tur(name_tur))
        FindStudentByNameOfTur.students.clear()

    elif choice == "2":
        print("type sport ")
        name_sport = input()
        print(StudentControllerImpl.find_student_by_sport(name_sport))
        FindStudentBySport.students.clear()

    elif choice == "3":
        print("winning size")
        name_size = input()
        print(StudentControllerImpl.find_student_by_winning_size(name_size))
        FindStudentByWinningSize.students.clear()

    elif choice == "4":
        print("type group number ")
        name_tur = input()
        print(StudentControllerImpl.delete_student_by_name_tur(name_tur))
    elif choice == "5":
        print("type sport ")
        name_sport = input()
        print(StudentControllerImpl.delete_student_by_sport(name_sport))
    elif choice == "6":
        print("winning size")
        name_size = input()
        print(StudentControllerImpl.delete_student_by_winning_size(name_size))
    elif choice == "7":
        break