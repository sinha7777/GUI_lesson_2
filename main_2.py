from tkinter import *
from tkinter.ttk import*
import time

root = Tk()

root.geometry("100x100")
root.title("progress bar")

progress = Progressbar(root,orient=HORIZONTAL,length=100,mode="determinate")
progress.pack(pady=10)

def bar():
    progress["value"]=20
    root.update_idletasks()
    time.sleep(1)

    progress["value"]=40
    root.update_idletasks()
    time.sleep(1)

    progress["value"]=60
    root.update_idletasks()
    time.sleep(1)

    progress["value"]=80
    root.update_idletasks()
    time.sleep(1)

    progress["value"]=100

btn = Button(root,text = "start", command=bar)
btn.pack(pady=10)

root.mainloop()