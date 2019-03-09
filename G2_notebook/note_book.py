# coding=utf-8
# 引入datetime以计算当前时间
import datetime

if __name__ == '__main__':
    # 创建一个循环, 允许用户无限次输入事情
    while True:
        thing = raw_input("请输入要记录的事(输入q就是退出): ")
        # 计算当前日期, 以拼接文件名
        today = datetime.datetime.today().strftime('%Y年%m月%d日') + "_记事本.txt"
        # 如果用户输入q的话，跳出循环
        if thing == "q":
            break
        # 立刻保存用户输入的数据
        with open(today, 'a') as the_file:
            the_file.write(thing + '\n')
