from tkinter import *

root = Tk()
root.geometry("100x100")
root.config(bg="white")
root.title("Spinbox")

s = Spinbox(root,from_=0,to=100)
s.pack()

root.mainloop()
