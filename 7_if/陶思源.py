if __name__ == '__main__':
    user_surname = raw_input("Please enter your surname: ")
    user_name = raw_input("Please enter your name: ")
    print "{" + user_surname + "} - {" + user_name + "}"
    print "{%s} - {%s}" % (user_surname, user_name)
