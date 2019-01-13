# coding=utf-8
import random

if __name__ == '__main__':
    # 创建一个随机数，给用户来猜
    secret = random.randint(1, 100)

    # 规定最大猜的次数
    max_trials = 6

    # 储存用户最近一次猜的数
    guess = []

    for i in range(0, max_trials):
        # 提示用户输入猜的数
        guess = raw_input("Please input your guess: ")

        # 判断用户猜的数正确
        if guess == secret:
            print "你猜对了! 次数 = ", i + 1
            break
        # 判断用户猜小了
        elif guess < secret:
            print "你猜的数", guess, "太小了!"
        # 判断用户猜大了
        else:
            print "你猜的数", guess, "太大了!"

    # 结束循环时判断猜的数是否正确
    if secret != guess:
        print "你的次数用完了，正确的数是", secret
