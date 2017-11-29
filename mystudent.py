import unittest

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


    def get_grade(self):
        if self.score >= 60 and self.score < 80:
            return 'B'
        if self.score >= 80 and self.score <= 100:
            return 'A'
        if self.score >= 0 and self.score <60:
            return 'C'
        if self.score < 0 or self.score > 100:
            raise ValueError('Invalid score value')


class TestStudent(unittest.TestCase):
    def test_80_to_100(self):
        s1 = Student('Bob', 80)
        s2 = Student('Bat', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bob', 60)
        s2 = Student('Bat', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bob', 0)
        s2 = Student('Bat', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bob', -1)
        s2 = Student('Bat', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()


if __name__ == '__main__':
    unittest.main()


