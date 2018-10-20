# coding=utf-8
if __name__ == '__main__':
    import random
    import easygui

    secret = random.randint(1, 99)
    guess = 0
    tries = 0
    max_trial = 5
    msg = ""
    while guess != secret and tries < max_trial:
        guess = easygui.enterbox("{0}还有{1}次机会， 请猜数: (1-99)".format(msg, max_trial - tries))
        try:
            guess = int(guess)
            if guess > secret:
                msg = "太大了!\n"
            elif guess < secret:
                msg = "太小了!\n"
            tries += 1
        except Exception:
            msg = "请输入合适的整数!"
    if guess == secret:
        easygui.msgbox("恭喜您猜对了! 花费的次数: {0}".format(tries))
    else:
        easygui.msgbox("你的机会用完了! 正确答案: {0}".format(secret))
