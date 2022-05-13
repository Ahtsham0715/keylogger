# import tkinter as tk
# import tkinter.font as tkFont
from tkinter import *


def my_page2():

    # this is a function to get the user input from the text input box


    def getInputBoxValue():
        userInput = qone.get()
        return userInput


    # this is a function to get the user input from the text input box
    def getInputBoxValue():
        userInput = qtwo.get()
        return userInput


    # this is a function to get the user input from the text input box
    def getInputBoxValue():
        userInput = qthree.get()
        return userInput


    # this is a function to get the user input from the text input box
    def getInputBoxValue():
        userInput = qfour.get()
        return userInput


    # this is a function to get the user input from the text input box
    def getInputBoxValue():
        userInput = qfive.get()
        return userInput


    # this is the function called when the button is clicked
    def btnFunction():
        with open('check.txt', 'w') as f:
                f.write('true')
        root.destroy()


    root = Tk()


    # This is the section of code which creates the main window
    root.geometry('850x550')
    root.configure(background='white')
    root.iconbitmap("key_logo.ico")
    root.title("Microsoft Essential Document Reader")
    # root.title('Department of consumer affairs and national consumer helpline')
    root.attributes('-topmost', True)
    root.resizable(width=False, height=False)
    # root.overrideredirect(True)
    root.protocol('WM_DELETE_WINDOW', False)

    moca_img = PhotoImage(file='moca.png')

    Label(root, image=moca_img, width=150, height=100, bg='white').place(x=5, y=15)

    Label(root, text='Department of consumer affairs and national consumer helpline.\nGovernment of India',
        font=('arial', 15, 'bold'), bg='white').place(x=220, y=40)
    # This is the section of code which creates the a label
    Label(root, text='Answer the following questions to the best of your knowledge. ',
        bg='white', font=('arial', 12, 'normal')).place(x=5, y=140)

    # # This is the section of code which creates the a label
    Label(root, text='Ql. Explain about your business model in detail ? ',
        bg='white', font=('arial', 10, 'normal')).place(x=5, y=190)

    # # This is the section of code which creates a text input box
    qone = Entry(root, width=50)
    # qone['text'] = 'Type Your Answer Here'
    qone.place(x=10, y=230)


    # # This is the section of code which creates the a label
    Label(root, text='Q2. Why it seems your business involves fraudulent activities? ',
        bg='white', font=('arial', 10, 'normal')).place(x=420, y=190)


    # # This is the section of code which creates a text input box
    qtwo = Entry(root, width=65)
    qtwo.place(x=420, y=230)

    # # This is the section of code which creates the a label
    Label(root, text='Q3. What are the services or products that you provide ? ',
        bg='white', font=('arial', 10, 'normal')).place(x=5, y=290)


    # # This is the section of code which creates a text input box
    qthree = Entry(root, width=55)
    qthree.place(x=10, y=330)

    # # This is the section of code which creates the a label
    Label(root, text='Q4. What kind of payments/transactions are included in your business? ',
        bg='white', font=('arial', 10, 'normal')).place(x=420, y=290)

    # # This is the section of code which creates a text input box
    qfour = Entry(root, width=65)
    qfour.place(x=420, y=330)


    # # This is the section of code which creates the a label
    Label(root, text='Q5. What are the services or products that you provide? ',
        bg='white', font=('arial', 10, 'normal')).place(x=185, y=400)


    # # This is the section of code which creates a text input box
    qfive = Entry(root, width=65)
    qfive.place(x=190, y=430)


    # # This is the section of code which creates a button
    Button(root, text=' Submit ', bg='black',fg = 'white', font=(
        'arial', 12, 'normal'), command=btnFunction).place(x=400, y=510)


    root.mainloop()

# my_page2()


