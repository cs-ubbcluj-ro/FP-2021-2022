import unittest

from lecture.examples.ex24_gui.domain.entities import Student, Address
from lecture.examples.ex24_gui.domain.validators import StudentValidator, ValidationException


class TestStudentValidator(unittest.TestCase):
    def test_validate_student(self):
        val = StudentValidator()
        # student invalid if id is empty
        st = Student("", "Ion", Address("Adr", 1, "Cluj"))
        try:
            val.validate(st)
            self.assertFalse()
        except ValidationException:
            pass

        # student invalid if name is empty
        st = Student("3", "", Address("Adr", 1, "Cluj"))
        try:
            val.validate(st)
            self.assertFalse()
        except ValidationException:
            pass

        # student invalid if adr is empty
        st = Student("3", "Ion", Address("", 1, "Cluj"))
        try:
            val.validate(st)
            self.assertFalse()
        except ValidationException:
            pass
