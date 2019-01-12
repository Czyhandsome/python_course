# coding=utf-8
import random

if __name__ == '__main__':
    # 创建一个1-100的随机数
    secret = random.randint(1, 100)
    # 变量, 用于储存用户已经尝试的次数
    trial = 0
    # 用户可以尝试的最大次数
    max_trial = 6
    # 用户猜的数
    guess = 0
    # 用户最多可以猜max_trial次
    while trial < max_trial:
        # 用户猜的次数+1
        trial = trial + 1
        # 引导用户输入要猜的值
        guess = input("Please input your guess: ")
        # 判断用户猜的数是否正确
        if guess == secret:
            print "You are right! Trials: ", trial
            break
        # 用户猜的数太大的情况
        elif guess > secret:
            print "Your guess", guess, "is too big!"
        # 用户猜的数太小了
        else:
            print "Your guess", guess, "is too small!"
    # 如果用户最后还没猜出来，给出最终结果
    if guess != secret:
        print "You ran out of guesses! Answer: ", secret
