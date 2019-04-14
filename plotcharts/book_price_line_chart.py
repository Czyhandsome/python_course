# coding=utf-8
import matplotlib.pyplot as plt


def book_price(_num):
    """
    根据书的数量计算价格
    """
    return _num * 10


if __name__ == '__main__':
    x = [1, 2, 3, 4]
    y = map(book_price, x)
    fig = plt.figure()

    plt.title("Book price line chart")
    plt.xlabel("Number of books")
    plt.ylabel("Book price")
    plt.plot(x, y)
    plt.show()
