# coding=utf-8
import random

if __name__ == '__main__':
    secret = random.randint(1, 99)
    MAX_TRIALS = 6
    print("""猜一个1到99之间的数字!
    你有{0}次机会可以猜这个数字""".format(MAX_TRIALS))
    tries = 0
    guess = 0
    while tries < MAX_TRIALS and guess != secret:
        try:
            guess = int(input("请输入猜测的数字: "))
            tries = tries + 1
            if guess < secret:
                print("第{0}次猜的不对: 猜的数小于正确答案!".format(tries))
            elif guess > secret:
                print("第{0}次猜的不对: 猜的数大于正确答案!".format(tries))
        except ValueError:
            print("请输入正确的数字!")
    if guess == secret:
        print("恭喜你猜对了! 花费的次数: {0}次".format(tries))
    else:
        print("很遗憾, 你没有在{0}次之内猜对正确答案!".format(MAX_TRIALS))
        print("正确答案是: {0}".format(secret))
