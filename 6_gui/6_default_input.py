if __name__ == '__main__':
    import easygui

    flavor = easygui.enterbox('What is your favourite flavor?',
                              default='Yogurt')
    easygui.msgbox("Your entered: " + flavor)
