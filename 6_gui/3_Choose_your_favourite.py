if __name__ == '__main__':
    import easygui

    # Guide user to choose from 3 flavors
    flavor = easygui.buttonbox('What is your favourite ice cream flavor?',
                               choices=['Vanilla', 'Chocolate', 'Strawberry'])
    # Show the flavor which user chose
    easygui.msgbox("You clicked: " + flavor)
