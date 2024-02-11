import tkinter as tk

# background = #222224
# accent = #5828d1
# highlight = #d4601e

window = tk.Tk()
window.title("CODSOFT Task 2")
window.geometry("440x540")
window.configure(bg="#FFFFFF")

frame = tk.Frame(bg="#FFFFFF")

disp = tk.Entry(frame, font=("Arial", 30), bg="#FFFFFF", fg="#222224", bd=0)
label = tk.Label(frame, text="Calculator", fg="#222224", bg="#FFFFFF", font=("Arial", 30), pady=10)
label.grid(row=0, column=0, columnspan=4)
# geometry managers --> pack, place, grid
disp.grid(row=1, columnspan=4, pady=10)

def button_click(s): 
    match s: 
        case "=": 
            try: 
                result = eval(disp.get())
                disp.delete(0, tk.END)
                disp.insert(tk.END, str(result))
            except: 
                disp.delete(0, tk.END)
                disp.insert(tk.END, "error")
        case "C": 
            disp.delete(0, tk.END)
        case _:
            disp.insert(tk.END, s)

button1 = tk.Button(frame, text= "1", fg="purple", bg="yellow",command=lambda: button_click(1), height=3, width=4, font=('Arial', 20), bd=0) 
button1.grid(row=3, column=0, pady=5) 

button2 = tk.Button(frame, text='2', fg="purple", bg="yellow", command=lambda: button_click(2), height=3, width=4, font=('Arial', 20), bd=0) 
button2.grid(row=3, column=1, pady=5) 

button3 = tk.Button(frame, text='3', fg="purple", bg="yellow", command=lambda: button_click(3), height=3, width=4, font=('Arial', 20), bd=0) 
button3.grid(row=3, column=2, pady=5) 

button4 = tk.Button(frame, text='4', fg="purple", bg="yellow", command=lambda: button_click(4), height=3, width=4, font=('Arial', 20), bd=0) 
button4.grid(row=4, column=0, pady=5) 

button5 = tk.Button(frame, text='5', fg="purple", bg="yellow", command=lambda: button_click(5), height=3, width=4, font=('Arial', 20), bd=0) 
button5.grid(row=4, column=1, pady=5) 

button6 = tk.Button(frame, text='6', fg="purple", bg="yellow", command=lambda: button_click(6), height=3, width=4, font=('Arial', 20), bd=0) 
button6.grid(row=4, column=2, pady=5) 

button7 = tk.Button(frame, text='7', fg="purple", bg="yellow", command=lambda: button_click(7), height=3, width=4, font=('Arial', 20), bd=0) 
button7.grid(row=5, column=0, pady=5) 

button8 = tk.Button(frame, text='8', fg="purple", bg="yellow", command=lambda: button_click(8), height=3, width=4, font=('Arial', 20), bd=0) 
button8.grid(row=5, column=1, pady=5) 

button9 = tk.Button(frame, text='9', fg="purple", bg="yellow", command=lambda: button_click(9), height=3, width=4, font=('Arial', 20), bd=0) 
button9.grid(row=5, column=2, pady=5) 

button0 = tk.Button(frame, text='0', fg="purple", bg="yellow", command=lambda: button_click(0), height=3, width=4, font=('Arial', 20), bd=0) 
button0.grid(row=6, column=0, pady=5) 

buttonEquals = tk.Button(frame, text="=", fg="red", bg="yellow", command=lambda: button_click("="), height=3, width=4, font=('Arial', 20), bd=0)
buttonEquals.grid(row=6, column=1, pady=5)

buttonClear = tk.Button(frame, text="C", fg="purple", bg="yellow", command=lambda: button_click("C"), height=3, width=4, font=('Arial', 20), bd=0)
buttonClear.grid(row=6, column=2, pady=5)

buttonAdd = tk.Button(frame, text="+", fg="purple", bg="yellow", command=lambda: button_click("+"), height=3, width=4, font=('Arial', 20), bd=0)
buttonAdd.grid(row=3, column=3, pady=5)

buttonSub = tk.Button(frame, text="-", fg="purple", bg="yellow", command=lambda: button_click("-"), height=3, width=4, font=('Arial', 20), bd=0)
buttonSub.grid(row=4, column=3, pady=5)

buttonMul = tk.Button(frame, text="*", fg="purple", bg="yellow", command=lambda: button_click("*"), height=3, width=4, font=('Arial', 20), bd=0)
buttonMul.grid(row=5, column=3, pady=5)

buttonDiv = tk.Button(frame, text="/", fg="purple", bg="yellow", command=lambda: button_click("/"), height=3, width=4, font=('Arial', 20), bd=0)
buttonDiv.grid(row=6, column=3, pady=5)

# mainloop must be the last statement, as it will only allow everything before it to run until the window is closed.
frame.pack()
window.mainloop()