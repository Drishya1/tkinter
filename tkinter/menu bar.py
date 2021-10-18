from tkinter import *

root= Tk()
root.geometry('555x333')
root.title('drishya menu')
def dady():
    print("i am yo daddy")


#for ceating menu

mymenu = Menu(root)
mymenu.add_command(label='File',command=dady)
mymenu.add_command(label='Exit',command=quit)
root.config(menu = mymenu)


root.mainloop()