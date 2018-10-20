if __name__ == '__main__':
    import easygui

    choice = []
    i = 0
    while i < 50:
        i += 1
        choice.append("batminten {0}".format(i))

    sport = easygui.buttonbox('what\'s your favourite sports',
                              choices=choice)

    try:
        easygui.msgbox("you clicked: " + sport)
    except Exception as e:
        easygui.msgbox(e.message)
