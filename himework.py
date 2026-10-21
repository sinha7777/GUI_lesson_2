from tkinter import *

root = Tk()

root.geometry("700x500")
root.title("Food Delivery App")
root.config(bg="red")

email_label = Label(root, text="Email")
email_label.place(x=100, y=40)

email_entry = Entry(root, width=40)
email_entry.place(x=180, y=40)

password_label = Label(root, text="Password")
password_label.place(x=100, y=80)

password_entry = Entry(root, width=40, show="*")
password_entry.place(x=180, y=80)

food_label = Label(root, text="What food would you like: Chicken Sandwich, B.L.T, Veg Sandwich or None?")
food_label.place(x=80, y=150)

food_entry = Entry(root, width=35)
food_entry.place(x=80, y=180)

s1 = Spinbox(root, from_=1, to=4, width=5)
s1.place(x=500, y=180)

drink_label = Label(root, text="What beverage would you like: Cola, Fanta, Orange Juice, Water or None?")
drink_label.place(x=80, y=240)

drink_entry = Entry(root, width=35)
drink_entry.place(x=80, y=270)

s2 = Spinbox(root, from_=1, to=5, width=5)
s2.place(x=500, y=270)

dessert_label = Label(root, text="What dessert would you like: Ice Cream, Ice Lolly, Chocolate Cake or None?")
dessert_label.place(x=80, y=330)

dessert_entry = Entry(root, width=35)
dessert_entry.place(x=80, y=360)

s3 = Spinbox(root, from_=1, to=5, width=5)
s3.place(x=500, y=360)

submit_button = Button(root, text="Submit Order")
submit_button.place(x=300, y=430)

root.mainloop()