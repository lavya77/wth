import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("400x500") 

entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)


def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))


def clear():
    entry.delete(0, tk.END)

def calculate():
    expr = entry.get()
    try:
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
    except Exception:
        messagebox.showerror("Error", "Invalid Expression!")


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '%', '+',
    'C', '**', '=', 
]


row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        b = tk.Button(root, text=button, width=8, height=3, font=('Arial', 18), command=calculate)
        b.grid(row=row_val, column=col_val, columnspan=2, padx=5, pady=5)
        col_val += 2
    elif button == 'C':
        b = tk.Button(root, text=button, width=8, height=3, font=('Arial', 18), command=clear)
        b.grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1
    else:
        b = tk.Button(root, text=button, width=8, height=3, font=('Arial', 18), command=lambda val=button: button_click(val))
        b.grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
