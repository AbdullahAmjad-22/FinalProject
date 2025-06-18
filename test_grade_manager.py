import unittest
from grade_manager import add_student, calculate_score

class TestGradeManager(unittest.TestCase):

    def test_add_student_valid(self):
        student = add_student("Ali", {"Math": 90})
        self.assertEqual(student['name'], "Ali")
        self.assertEqual(student['grades']["Math"], 90)

    def test_add_student_invalid_grades(self):
        with self.assertRaises(ValueError):
            add_student("Ali", ["Math", 90])  # Should raise ValueError

    def test_calculate_score(self):
        grades = {"Math": 90, "English": 80}
        gpa = calculate_score(grades)
        self.assertEqual(gpa, 85.0)

    def test_calculate_gpa_empty(self):
        self.assertEqual(calculate_score({}), 0)

if __name__ == '__main__':
    unittest.main()
