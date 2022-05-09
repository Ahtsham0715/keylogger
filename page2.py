# import tkinter as tk
# import tkinter.font as tkFont


# def my_page2():

#     root = tk.Tk()
#     #setting title
#     root.title("Department of consumer affairs and national consumer helpline")
#     #setting window size
#     width=600
#     height=500
#     screenwidth = root.winfo_screenwidth()
#     screenheight = root.winfo_screenheight()
#     alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
#     root.geometry(alignstr)
#     root.resizable(width=False, height=False)
#     root.overrideredirect(True)
#     GLabel_917=tk.Label(root)
#     ft = tkFont.Font(family='Times',size=12)
#     GLabel_917["font"] = ft
#     GLabel_917["fg"] = "#333333"
#     GLabel_917["justify"] = "center"
#     GLabel_917["text"] = "Answer the following questions to the best of your knowledge. "
#     GLabel_917.pack()

#     GLabel_265=tk.Label(root)
#     ft = tkFont.Font(family='Times',size=12)
#     GLabel_265["font"] = ft
#     GLabel_265["fg"] = "#333333"
#     GLabel_265["justify"] = "center"
#     GLabel_265["text"] = "Ql. Explain about your business model in detail ? "
#     GLabel_265.pack(pady=10)

#     GLine_82=tk.Entry(root)
#     # GLineEdit_82["borderwidth"] = "1px"
#     ft = tkFont.Font(family='Times',size=12)
#     GLine_82["font"] = ft
#     GLine_82["fg"] = "#333333"
#     GLine_82["justify"] = "left"
#     GLine_82["text"] = "Type Your Answer Here "
#     GLine_82["relief"] = "flat"
#     GLine_82.pack(pady=5)

#     # GLabel_799=tk.Label(root)
#     # ft = tkFont.Font(family='Times',size=12)
#     # GLabel_799["font"] = ft
#     # GLabel_799["fg"] = "#333333"
#     # GLabel_799["justify"] = "center"
#     # GLabel_799["text"] = "Q2. Why it seems your business involves fraudulent activities? "
#     # GLabel_799.pack(pady=10)

#     # GLineEdit_407=tk.Entry(root)
#     # # GLineEdit_407["borderwidth"] = "1px"
#     # ft = tkFont.Font(family='Times',size=12)
#     # GLineEdit_407["font"] = ft
#     # GLineEdit_407["fg"] = "#333333"
#     # GLineEdit_407["justify"] = "left"
#     # GLineEdit_407["text"] = "Type Your Answer Here "
#     # GLineEdit_407["relief"] = "flat"
#     # GLineEdit_407.pack(pady=5)

#     # GLabel_247=tk.Label(root)
#     # ft = tkFont.Font(family='Times',size=12)
#     # GLabel_247["font"] = ft
#     # GLabel_247["fg"] = "#333333"
#     # GLabel_247["justify"] = "center"
#     # GLabel_247["text"] = "Q3. What are the services or products that you provide ? "
#     # GLabel_247.pack(pady=10)

#     # GLineEdit_653=tk.Entry(root, validate=['focusin'])
#     # # GLineEdit_653["borderwidth"] = "1px"
#     # ft = tkFont.Font(family='Times',size=12)
#     # GLineEdit_653["font"] = ft
#     # GLineEdit_653["fg"] = "#333333"
#     # GLineEdit_653["justify"] = "left"
#     # GLineEdit_653["text"] = "Type Your Answer Here "
#     # GLineEdit_653["relief"] = "flat"
#     # GLineEdit_653.pack(pady=5)

#     GLabel_450=tk.Label(root)
#     ft = tkFont.Font(family='Times',size=12)
#     GLabel_450["font"] = ft
#     GLabel_450["fg"] = "#333333"
#     GLabel_450["justify"] = "center"
#     GLabel_450["text"] = "Q2. What kind of payments/transactions are included in your business? "
#     GLabel_450.pack(pady=10)

#     GLineEdit_411=tk.Entry(root)
#     # GLineEdit_411["borderwidth"] = "1px"
#     ft = tkFont.Font(family='Times',size=12)
#     GLineEdit_411["font"] = ft
#     GLineEdit_411["fg"] = "#333333"
#     GLineEdit_411["justify"] = "left"
#     GLineEdit_411["text"] = "Type Your Answer Here"
#     GLineEdit_411["relief"] = "flat"
#     GLineEdit_411.pack(pady=5)

#     def GButton_240_command():
#         with open('check.txt', 'w') as f:
#             f.write('true')
#         root.destroy()
#         # main_func
#     GButton_240=tk.Button(root)
#     GButton_240["bg"] = "#000000"
#     ft = tkFont.Font(family='Times',size=16)
#     GButton_240["font"] = ft
#     GButton_240["fg"] = "#ffffff"
#     GButton_240["justify"] = "center"
#     GButton_240["text"] = "Submit"
#     GButton_240.place(x=490,y=450,width=100)
#     GButton_240["command"] = GButton_240_command

#     root.mainloop()

# my_page2()

import tkinter as tk
from tkinter import ttk
from tkinter import *

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
    print('clicked')


root = Tk()

# This is the section of code which creates the main window
root.geometry('850x425')
root.configure(background='white')
root.title('Department of consumer affairs and national consumer helpline')
# root.overrideredirect(True)

# This is the section of code which creates a text input box
qone = Entry(root, width=45)
qone.place(x=5, y=99)


# This is the section of code which creates a text input box
qtwo = Entry(root, width=65)
qtwo.place(x=420, y=92)


# This is the section of code which creates a text input box
qthree = Entry(root, width=45)
qthree.place(x=5, y=184)


# This is the section of code which creates a text input box
qfour = Entry(root, width=65)
qfour.place(x=420, y=176)


# This is the section of code which creates a text input box
qfive = Entry(root, width=65)
qfive.place(x=190, y=308)


# This is the section of code which creates the a label
Label(root, text='Answer the following questions to the best of your knowledge. ',
      bg='white', font=('arial', 12, 'normal')).place(x=163, y=12)


# This is the section of code which creates the a label
Label(root, text='Ql. Explain about your business model in detail ? ',
      bg='white', font=('arial', 10, 'normal')).place(x=5, y=60)


# This is the section of code which creates the a label
Label(root, text='Q2. Why it seems your business involves fraudulent activities? ',
      bg='white', font=('arial', 10, 'normal')).place(x=420, y=61)


# This is the section of code which creates the a label
Label(root, text='Q3. What are the services or products that you provide ? ',
      bg='white', font=('arial', 10, 'normal')).place(x=5, y=142)


# This is the section of code which creates the a label
Label(root, text='Q4. What kind of payments/transactions are included in your business? ',
      bg='white', font=('arial', 10, 'normal')).place(x=420, y=138)


# This is the section of code which creates the a label
Label(root, text='Q5. What kind of payments/transactions are included in your business? ',
      bg='white', font=('arial', 10, 'normal')).place(x=185, y=266)


# This is the section of code which creates a button
Button(root, text='Submit', bg='black',fg = 'white', font=(
    'arial', 12, 'normal'), command=btnFunction).place(x=770, y=386)


root.mainloop()
