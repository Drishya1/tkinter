from tkinter import *

root = Tk()
root.geometry('555x333')
root.title('menu bar')
def daddy():
    print("hehe")

yourmenubar = Menu(root)

m1 = Menu(yourmenubar,tearoff=0)
m1.add_command(label='save',command = daddy)
m1.add_command(label='view',command = daddy)
m1.add_separator()
m1.add_command(label='edit',command = daddy)
m1.add_command(label='quit',command = quit)

root.config(menu = yourmenubar)
yourmenubar.add_cascade(label='File',menu = m1)

m2 = Menu(yourmenubar,tearoff=0)
m2.add_command(label='color correction',command = daddy)
m2.add_command(label='main edit',command = daddy)
m2.add_separator()
m2.add_command(label='bad edit',command = daddy)
m2.add_command(label='create',command = quit)

root.config(menu = yourmenubar)
yourmenubar.add_cascade(label='edit',menu = m2)

root.mainloop()
