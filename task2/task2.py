# # Design a simple calculator with basic arithmetic operations.
# # Prompt the user to input two numbers and an operation choice.
# # Perform the calculation and display the result.

# from tkinter import *
# from tkinter import ttk

# root = Tk()

# root.configure(background="blueviolet")
# root.title("Calculator")
# # root.geometry("400x300")
# # root.Frame(padding=20)
# expression = Entry(root, textvariable="hello world!")
# expression.grid(columnspan=6, ipadx=70)


# button1 = Button(root, text=' 1 ', fg='black', bg='red',command=lambda: press(1), height=1, width=7) 
# button1.grid(row=3, column=0) 

# button2 = Button(root, text=' 2 ', fg='black', bg='red', command=lambda: press(2), height=1, width=7) 
# button2.grid(row=3, column=1) 

# button3 = Button(root, text=' 3 ', fg='black', bg='red', command=lambda: press(3), height=1, width=7) 
# button3.grid(row=3, column=2) 

# button4 = Button(root, text=' 4 ', fg='black', bg='red', command=lambda: press(4), height=1, width=7) 
# button4.grid(row=4, column=0) 

# button5 = Button(root, text=' 5 ', fg='black', bg='red', command=lambda: press(5), height=1, width=7) 
# button5.grid(row=4, column=1) 

# button6 = Button(root, text=' 6 ', fg='black', bg='red', command=lambda: press(6), height=1, width=7) 
# button6.grid(row=4, column=2) 

# button7 = Button(root, text=' 7 ', fg='black', bg='red', command=lambda: press(7), height=1, width=7) 
# button7.grid(row=5, column=0) 

# button8 = Button(root, text=' 8 ', fg='black', bg='red', command=lambda: press(8), height=1, width=7) 
# button8.grid(row=5, column=1) 

# button9 = Button(root, text=' 9 ', fg='black', bg='red', command=lambda: press(9), height=1, width=7) 
# button9.grid(row=5, column=2) 

# button0 = Button(root, text=' 0 ', fg='black', bg='red', command=lambda: press(0), height=1, width=7) 
# button0.grid(row=6, column=0) 


# root.mainloop()
import tkinter as tk

def button_click(symbol):
    if symbol == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif symbol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 20), bd=5, bg="black", fg="green")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0, 1, 4)
]

for symbol, row, col, *args in buttons:
    button = tk.Button(root, text=symbol, width=5, height=2, font=("Arial", 20), bg="black", fg="green", command=lambda s=symbol: button_click(s))
    button.grid(row=row, column=col, rowspan=args[0] if args else 1, columnspan=args[1] if len(args) > 1 else 1)

root.mainloop()
