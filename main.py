from tkinter import *

clicked_bool = []
clicked_bool.append(False)
first = []
second = []
operation = []


def clicked_operation(current_operation, clicked_bool):
    operation.append(f'{current_operation}')
    clicked_bool[0] = True
    lbl.configure(text=f'{current_operation}')


def clicked_number(number, first, second, clicked_bool):
    if not clicked_bool[0]:
        first.append(f'{number}')
        lbl.configure(text=''.join(first))
    else:
        second.append(f'{number}')
        lbl.configure(text=''.join(second))


def clicked_calculation(operation, first, second):
    first1 = ''.join(first)
    second1 = ''.join(second)
    if operation[0] == '+':
        rez = int(first1) + int(second1)
    elif operation[0] == '-':
        rez = int(first1) - int(second1)
    elif operation[0] == '*':
        rez = int(first1) * int(second1)
    elif operation[0] == '/':
        rez = int(first1) / int(second1)
    lbl.configure(text=f"Ответ: {round(rez, 3)}")
    clicked_bool[0] = False
    operation.clear()
    first.clear()
    second.clear()


def clicked_clear(first, second):
    first.clear()
    second.clear()
    operation.clear()
    clicked_bool[0] = False
    lbl.configure(text="0")
    print(first, second)


window = Tk()
window.title("Python calculator")
window.geometry('335x380')
lbl = Label(window, text="0", font=('', 25))
lbl.place(x=10, y=0)
btn_0 = Button(window, text="0", width=10, height=3, command=lambda: clicked_number(0, first, second, clicked_bool))
btn_0.grid(column=1, row=7)
btn_1 = Button(window, text="1", width=10, height=3, command=lambda: clicked_number(1, first, second, clicked_bool))
btn_1.grid(column=0, row=6)
btn_2 = Button(window, text="2", width=10, height=3, command=lambda: clicked_number(2, first, second, clicked_bool))
btn_2.grid(column=1, row=6)
btn_3 = Button(window, text="3", width=10, height=3, command=lambda: clicked_number(3, first, second, clicked_bool))
btn_3.grid(column=2, row=6)
btn_4 = Button(window, text="4", width=10, height=3, command=lambda: clicked_number(4, first, second, clicked_bool))
btn_4.grid(column=0, row=5)
btn_5 = Button(window, text="5", width=10, height=3, command=lambda: clicked_number(5, first, second, clicked_bool))
btn_5.grid(column=1, row=5)
btn_6 = Button(window, text="6", width=10, height=3, command=lambda: clicked_number(6, first, second, clicked_bool))
btn_6.grid(column=2, row=5)
btn_7 = Button(window, text="7", width=10, height=3, command=lambda: clicked_number(7, first, second, clicked_bool))
btn_7.grid(column=0, row=4)
btn_8 = Button(window, text="8", width=10, height=3, command=lambda: clicked_number(8, first, second, clicked_bool))
btn_8.grid(column=1, row=4)
btn_9 = Button(window, text="9", width=10, height=3, command=lambda: clicked_number(9, first, second, clicked_bool))
btn_9.grid(column=2, row=4)
btn_plus = Button(window, text="+", width=10, height=3, command=lambda: clicked_operation('+', clicked_bool))
btn_plus.grid(column=3, row=2)
btn_sub = Button(window, text="-", width=10, height=3, command=lambda: clicked_operation('-', clicked_bool))
btn_sub.grid(column=3, row=3)
btn_div = Button(window, text="/", width=10, height=3, command=lambda: clicked_operation('/', clicked_bool))
btn_div.grid(column=3, row=4)
btn_mult = Button(window, text="*", width=10, height=3, command=lambda: clicked_operation('*', clicked_bool))
btn_mult.grid(column=3, row=5)
btn_calculation = Button(window, text="=", width=10, height=3, command=lambda: clicked_calculation(operation, first, second))
btn_calculation.grid(column=3, row=6)
btn_C = Button(window, text="C", width=10, height=3, command=lambda: clicked_clear(first, second))
btn_C.grid(column=3, row=7)
window.mainloop()
