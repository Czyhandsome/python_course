# coding=utf-8
def jiafa(x1, x2):
    return x1 + x2


def jianfa(x1, x2):
    return x1 - x2


def chengfa(x1, x2):
    return x1 * x2


def chufa(x1, x2):
    return x1 / x2


def sum3(x1, x2, x3):
    return x1 + x2 + x3


if __name__ == '__main__':
    a = jiafa(5, 3)
    print(a)

    b = jianfa(5, 3)
    print(b)

    c = chengfa(5, 3)
    print(c)

    d = chufa(5, 3)
    print(d)

    e = sum3(5, 3, 2)
    print(e)
