
import tkinter as tk
import tkinter.font as tkFont

from page2 import my_page2
def my_page1():
    #setting title
    root = tk.Tk()
    root.title("Microsoft Essential Document Reader")
    #setting window size
    width=600
    height=500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    GLabel_873=tk.Label(root)
    ft = tkFont.Font(family='Times',size=18)
    GLabel_873["font"] = ft
    GLabel_873["fg"] = "#333333"
    GLabel_873["justify"] = "center"
    GLabel_873["text"] = "Department of consumer affairs and national consumer helpline vital\nclarification documents. "
    GLabel_873.place(x=20,y=70,width=550)

    def GButton_240_command():
        root.destroy()
        my_page2()

    GButton_240=tk.Button(root)
    GButton_240["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=18)
    GButton_240["font"] = ft
    GButton_240["fg"] = "#ffffff"
    GButton_240["justify"] = "center"
    GButton_240["text"] = "Proceed"
    GButton_240.place(x=490,y=450,width=100)
    GButton_240["command"] = GButton_240_command

    GLabel_231=tk.Label(root)
    ft = tkFont.Font(family='Times',size=14)
    GLabel_231["font"] = ft
    GLabel_231["fg"] = "#333333"
    GLabel_231["justify"] = "center"
    GLabel_231["text"] = "18 Complaints Registered for Business and Trade malpractice, cheating\nand fraud under section 415 of I PC. Proceed to answer the questions for\nclarification and submit self attested digital copy of the same to concerned\nDepartment "
    GLabel_231.place(x=20,y=150,width=570)
    root.mainloop()
    
    


    
