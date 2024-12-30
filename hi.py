from tkinter import *

root = Tk()
root.title("Arun's Calculator")

e = Entry(root, width=35, borderwidth=4, bg="grey", fg="white")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

f_num = None
math = None

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_addition():
    first_number = e.get()
    global f_num, math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtraction():
    first_number = e.get()
    global f_num, math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiplication():
    first_number = e.get()
    global f_num, math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_division():
    first_number = e.get()
    global f_num, math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_num = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_num))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_num))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_num))
    elif math == "division":
        if int(second_num) != 0:
            e.insert(0, f_num / int(second_num))
        else:
            e.insert(0, "Error")

def button_clear():
    e.delete(0, END)

button_1 = Button(root, text="1", padx=30, pady=14, command=lambda: button_click(1), bg="yellow")
button_2 = Button(root, text="2", padx=30, pady=14, command=lambda: button_click(2), bg="yellow")
button_3 = Button(root, text="3", padx=30, pady=14, command=lambda: button_click(3), bg="yellow")
button_4 = Button(root, text="4", padx=30, pady=14, command=lambda: button_click(4), bg="yellow")
button_5 = Button(root, text="5", padx=30, pady=14, command=lambda: button_click(5), bg="yellow")
button_6 = Button(root, text="6", padx=30, pady=14, command=lambda: button_click(6), bg="yellow")
button_7 = Button(root, text="7", padx=30, pady=14, command=lambda: button_click(7), bg="yellow")
button_8 = Button(root, text="8", padx=30, pady=14, command=lambda: button_click(8), bg="yellow")
button_9 = Button(root, text="9", padx=30, pady=14, command=lambda: button_click(9), bg="yellow")
button_0 = Button(root, text="0", padx=30, pady=14, command=lambda: button_click(0), bg="yellow")

button_add = Button(root, text="+", padx=30, pady=14, command=button_addition, bg="yellow")
button_sub = Button(root, text="-", padx=30, pady=14, command=button_subtraction, bg="yellow")
button_mul = Button(root, text="X", padx=30, pady=14, command=button_multiplication, bg="yellow")
button_div = Button(root, text="/", padx=30, pady=14, command=button_division, bg="yellow")

button_equal = Button(root, text="=", padx=30, pady=14, command=button_equal, bg="yellow")
button_clear = Button(root, text="Clear", padx=20, pady=14, command=button_clear, borderwidth=3, bg="yellow")

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=4, column=1)
button_sub.grid(row=5, column=0)
button_mul.grid(row=5, column=1)
button_div.grid(row=5, column=2)

button_equal.grid(row=4, column=2)
button_clear.grid(row=6, column=0, columnspan=3)

root.mainloop()
