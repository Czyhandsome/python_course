if __name__ == '__main__':
    import easygui

    # Select flavor
    flavor = easygui.choicebox('What is your favourite ice cream flavor?',
                               choices=['Vanilla', 'Chocolate', 'Strawberry'])

    # Show the flavor which user chose
    easygui.msgbox("You selected: " + flavor)
