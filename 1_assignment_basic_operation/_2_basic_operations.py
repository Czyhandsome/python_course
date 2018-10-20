from play_ground_utils import todo_task


class Task02:
    add = 0
    minus = 0
    multiply = 0

    @staticmethod
    def task02():
        """
        整数的运算
        """
        a = 12
        b = 13
        Task02.add = todo_task("计算a与b的和")
        Task02.minus = todo_task("计算a与b的差")
        Task02.multiply = todo_task("计算a与b的乘积")
