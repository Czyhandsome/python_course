if __name__ == '__main__':
    import random

    secret = random.randint(1, 99)

    max_try = 6
    for i in range(0, max_try):
        user_guess = raw_input("Pleas enter your guess:")
        if secret == user_guess:
            print "You're right"
            break
        elif secret > user_guess:
            print "Too small"
        elif secret < user_guess:
            print "Too big"
    if secret != user_guess:
        print "You're wrong"
