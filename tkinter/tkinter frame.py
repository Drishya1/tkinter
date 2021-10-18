from tkinter import*

root = Tk()
root.geometry("433x233")

f1 = Frame(root,bg = 'grey',borderwidth = 6,relief = SUNKEN)
f1.pack(side = LEFT,fill = 'y')

f2 = Frame(root,bg='grey' ,borderwidth= 9,relief = SUNKEN)
f2.pack(side = TOP,fill = 'x')
l = Label(f1, text = "my name is drishya")
l.pack(pady = 140)
l = Label(f2, text = "k cha sathhhi")
l.pack(padx = 140)




root.mainloop()
