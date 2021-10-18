from tkinter import*
from PIL import Image,ImageTk

root =Tk()
root.geometry('888x666')


f1 = Frame(root,width = 600,height = 400)
Label(f1,text='Drishya daily',font = 'lucida 33 bold').pack()
f1.pack(side =TOP)
Label(f1 ,text ='july 16th 2020',font = 'lucida 10 bold').pack()

photo = Image.open('jp1.jpg')
picture = ImageTk.PhotoImage(photo)
image = Label(Image= picture)
image.pack()

root.mainloop()