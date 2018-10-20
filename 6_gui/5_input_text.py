if __name__ == '__main__':
    import easygui

    flavor = easygui.enterbox('What is your favourite flavor?')
    easygui.msgbox("Your entered: " + flavor)
