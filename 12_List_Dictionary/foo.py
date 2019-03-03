# coding=utf-8
if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    # 先检查一下3是否在列表中
    if 3 in a:
        # 查找3在列表中的位置
        print a.index(3)
    else:
        print '3不在列表中!'
