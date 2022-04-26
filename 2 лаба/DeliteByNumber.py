from xml.dom import minidom


class DeleteByNumber:

    def __init__(self, student_number: str):
        self._student_number = student_number

    def delete_student_by_student_id(self) -> bool:

        xml = minidom.parse('DataTable.xml')
        group = xml.documentElement

        try:
            students = group.getElementsByTagName('player')

            for student in students:
                if str(student.getAttribute('number')) == str(self._student_number):
                    student.parentNode.removeChild(student)

                    xml.writexml(open('DataTable.xml', 'w'))

                    return True
        except Exception:
            return False
