from tkinter import *

global clicked_bool
clicked_bool = False
global first
first = ''
global second
second = ''
global operation
operation = ''

def clicked_sum():
    operation = '+'
    clicked_bool = True

def clicked_sub():
    operation = '-'
    clicked_bool = True
    lbl.configure(text="Я же ")

def clicked_div():
    operation = '/'
    clicked_bool = True
    lbl.configure(text="Я ж")

def clicked_mult():
    operation = '*'
    clicked_bool = True
    lbl.configure(text="Я же .")

def clicked_one(first, clicked_bool, second):
    if not clicked_bool:
        first += '1'
        lbl.configure(text=first)
    else:
        second += '1'
        lbl.configure(text=second)

def clicked_two(first, clicked_bool, second):
    if not clicked_bool:
        first += '2'
        lbl.configure(text=first)
    else:
        second += '2'
        lbl.configure(text=second)

def clicked_three(first, clicked_bool, second):
    if not clicked_bool:
        first += '3'
        lbl.configure(text=first)
    else:
        second += '3'
        lbl.configure(text=second)

def clicked_four(first, clicked_bool, second):
    if not clicked_bool:
        first += '4'
        lbl.configure(text=first)
    else:
        second += '4'
        lbl.configure(text=second)

def clicked_five(first, clicked_bool, second):
    if not clicked_bool:
        first += '5'
        lbl.configure(text=first)
    else:
        second += '5'
        lbl.configure(text=second)

def clicked_six(first, clicked_bool, second):
    if not clicked_bool:
        first += '6'
        lbl.configure(text=first)
    else:
        second += '6'
        lbl.configure(text=second)

def clicked_seven(first, clicked_bool, second):
    if not clicked_bool:
        first += '7'
        lbl.configure(text=first)
    else:
        second += '7'
        lbl.configure(text=second)

def clicked_eight(first, clicked_bool, second):
    if not clicked_bool:
        first += '8'
        lbl.configure(text=first)
    else:
        second += '8'
        lbl.configure(text=second)

def clicked_nine(first, clicked_bool, second):
    if not clicked_bool:
        first += '9'
        lbl.configure(text=first)
    else:
        second += '9'
        lbl.configure(text=second)

def clicked_zero(first, clicked_bool, second):
    if not clicked_bool:
        first += '0'
        lbl.configure(text=first)
    else:
        second += '0'
        lbl.configure(text=second)

def clicked_operation():
    if operation == '+':
        rez = int(first) + int(second)
    elif operation == '-':
        rez = int(first) - int(second)
    elif operation == '*':
        rez = int(first) * int(second)
    elif operation == '/':
        rez = int(first) / int(second)
    lbl.configure(text=rez)
def clicked_clear():
    first = ''
    second = ''

window = Tk()
window.title("Python calculator")
window.geometry('335x380')
lbl = Label(window, text="", font=('', 25))
lbl.grid(column=2, row=0)
btn_0 = Button(window, text="0", width=10, height=3, command=clicked_zero)
btn_0.grid(column=1, row=7)
btn_1 = Button(window, text="1", width=10, height=3, command=lambda: clicked_one(first, clicked_bool, second))
btn_1.grid(column=0, row=6)
btn_2 = Button(window, text="2", width=10, height=3, command=lambda: clicked_two(first, clicked_bool, second))
btn_2.grid(column=1, row=6)
btn_3 = Button(window, text="3", width=10, height=3, command=lambda: clicked_three(first, clicked_bool, second))
btn_3.grid(column=2, row=6)
btn_4 = Button(window, text="4", width=10, height=3, command=lambda: clicked_four(first, clicked_bool, second))
btn_4.grid(column=0, row=5)
btn_5 = Button(window, text="5", width=10, height=3, command=lambda: clicked_five(first, clicked_bool, second))
btn_5.grid(column=1, row=5)
btn_6 = Button(window, text="6", width=10, height=3, command=lambda: clicked_six(first, clicked_bool, second))
btn_6.grid(column=2, row=5)
btn_7 = Button(window, text="7", width=10, height=3, command=lambda: clicked_seven(first, clicked_bool, second))
btn_7.grid(column=0, row=4)
btn_8 = Button(window, text="8", width=10, height=3, command=lambda: clicked_eight(first, clicked_bool, second))
btn_8.grid(column=1, row=4)
btn_9 = Button(window, text="9", width=10, height=3, command=lambda: clicked_nine(first, clicked_bool, second))
btn_9.grid(column=2, row=4)
btn_plus = Button(window, text="+", width=10, height=3, command=lambda: clicked_sum(operation, clicked_bool))
btn_plus.grid(column=3, row=2)
btn_sub = Button(window, text="-", width=10, height=3, command=clicked_sub)
btn_sub.grid(column=3, row=3)
btn_div = Button(window, text="/", width=10, height=3, command=clicked_div)
btn_div.grid(column=3, row=4)
btn_mult = Button(window, text="*", width=10, height=3, command=clicked_mult)
btn_mult.grid(column=3, row=5)
btn_operation = Button(window, text="=", width=10, height=3, command=clicked_operation)
btn_operation.grid(column=3, row=6)
btn_C = Button(window, text="C", width=10, height=3, command=clicked_clear)
btn_C.grid(column=3, row=7)
window.mainloop()
