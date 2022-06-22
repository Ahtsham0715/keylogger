
from tkinter import *



from page2 import my_page2
def my_page1():
    #setting title
    root = Tk()
    root.title("Microsoft Essential Document Reader")
    root.geometry('950x550')
    root.config(bg = 'white')
    root.iconbitmap("key_logo.ico")
    root.resizable(width=False, height=False)
    root.attributes('-topmost', True)
    # root.overrideredirect(True)
    root.protocol('WM_DELETE_WINDOW', False)
    
    moca_img = PhotoImage(file='moca1.png')

    Label(root, image=moca_img, width=300, height=200, bg='white').place(x=270, y=5)

    Label(root, text='Department of consumer affairs and national consumer helpline vital\nclarification documents.',
        font=('arial', 15, 'bold'), bg='white').place(x=90, y=210)

    
    Label(root, text='18 Complaints Registered for Business and Trade malpractice, cheating\nand fraud under section 415 of I PC. Proceed to answer the questions for\nclarification and submit self attested digital copy of the same to concerned\nDepartment',
        font=('arial', 15, 'normal'), bg='white').place(x=80, y=290)

    
    Label(root, text='Disclaimer. The content of this document is confidential and intended for the recipient specified in the document only. It is strictly forbidden to share any\npart of this document with any third party without a written consent of the victims. Unauthorized use disclosure or copying of this document or any part\nthereof is strictly prohibited and is unlawful',
        font=('arial', 9, 'normal'), justify=LEFT, bg='white').place(x=5, y=430)

    
    def btnFunction():
        root.destroy()
        my_page2()

    Button(root, text=' Proceed ', bg='black',fg = 'white', font=(
        'arial', 12, 'normal'), command=btnFunction).place(x=820, y=510)
    
    root.mainloop()
    
    
# my_page1()
    
