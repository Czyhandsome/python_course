# coding=utf-8
from unittest import TestCase

from play_ground_utils import todo_task


def number_compare(num):
    if todo_task("判断num是否大于5"):
        return True
    else:
        return False


class Quiz01(TestCase):
    def test_number_format(self):
        self.assertFalse(number_compare(0))
        self.assertFalse(number_compare(5))
        self.assertTrue(number_compare(6))
