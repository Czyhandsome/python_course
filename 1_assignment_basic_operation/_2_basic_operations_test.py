import unittest

from ._2_basic_operations import Task02


class Task02Test(unittest.TestCase):

    def test_task02(self):
        Task02.task02()
        self.assertEqual(25, Task02.add)
        self.assertEqual(-1, Task02.minus)
        self.assertEqual(156, Task02.multiply)


if __name__ == '__main__':
    unittest.main()
