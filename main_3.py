from tkinter import*
from tkinter.ttk import*

root = Tk()
root.geometry("400x400")
root.title("Menu")

menu_bar = Menu(root)

file = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file)

file.add_command(label="new File",command=None)
file.add_command(label="Open...",command=None)
file.add_command(label="Save",command=None)

file.add_separator()
file.add_command(label="Exit",command=root.destroy)

#-----------------------------------------------------------------------------------------------------

edit = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit",menu=edit)

edit.add_command(label="Undo",command=None)
edit.add_command(label="Redo",command=None)

edit.add_separator()
edit.add_command(label="Cut",command=None)
edit.add_command(label="Copy",command=None)

#-----------------------------------------------------------------------------------------------------

veiw = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Veiw",menu=veiw)

veiw.add_command(label="Command Palette",command=None)
veiw.add_command(label="Open View",command=None)

veiw.add_separator()

veiw.add_command(label="Run",command=None)
veiw.add_command(label="Chat",command=None)


root.config(menu = menu_bar)
root.mainloop()