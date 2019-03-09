# coding=utf-8
import random

if __name__ == '__main__':
    # 创建要猜的数字
    secret = random.randint(1, 99)
    # 规定最大猜的次数
    max_trials = 6
    # 开始循环, 最多循环6次
    user_guess = []
    for i in range(0, max_trials):
        # 引导用户输入要猜的数字
        user_guess = int(raw_input("Please write down your guess: "))
        # 判断猜的数与secret的关系
        if user_guess > secret:
            print "Too big!"
        elif user_guess < secret:
            print "Too small!"
        elif user_guess == secret:
            print "You are right!"
            break
    # 判断用户是否没猜对
    if user_guess != secret:
        print "secret is ", secret
