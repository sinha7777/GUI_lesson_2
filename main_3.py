from tkinter import *

root=Tk()

root.geometry("400x400")
root.title("scrollwheel")

label = Label(root,text="welcome",bg="white",fg="black")
label.pack()

scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT,fill=Y)

listbox = Listbox(root,yscrollcommand=scroll_bar.set)
for i in range(1,101):
    listbox.insert(END,"hi"+str(i))
listbox.pack()

scroll_bar.config(command=listbox.yview)


root.mainloop()