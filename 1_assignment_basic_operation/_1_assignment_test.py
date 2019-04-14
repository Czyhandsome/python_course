 import unittest

from _1_assignment import task01


class AssignmentTest(unittest.TestCase):
    def test_task01(self):
        self.assertEqual(task01(), 3)


if __name__ == '__main__':
    unittest.main()
