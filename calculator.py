import tkinter as tk
import math

root = tk.Tk()
root.title("iPhone-style Calculator")
root.geometry("400x600")
root.configure(bg="#000000")


def button_click(value):
    current = display.get()
    if current == "Error":
        current = ""
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(value))


def button_clear():
    display.delete(0, tk.END)


def button_delete():
    current = display.get()
    if current != "Error" and len(current) > 0:
        display.delete(len(current)-1, tk.END)


def button_sqrt():
    try:
        current = display.get()
        result = math.sqrt(float(current))
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def button_equal():
    try:
        current = display.get()
        result = eval(current)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")


display = tk.Entry(root, font=('Arial', 24), bg="#000000", fg="white", borderwidth=0, justify='right')
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, sticky='nsew')


buttons = [
    ('C', button_clear, '#505050'), ('√', button_sqrt, '#505050'), ('%', lambda: button_click('%'), '#505050'), ('÷', lambda: button_click('/'), '#FF9500'),
    ('7', lambda: button_click('7'), '#505050'), ('8', lambda: button_click('8'), '#505050'), ('9', lambda: button_click('9'), '#505050'), ('×', lambda: button_click('*'), '#FF9500'),
    ('4', lambda: button_click('4'), '#505050'), ('5', lambda: button_click('5'), '#505050'), ('6', lambda: button_click('6'), '#505050'), ('-', lambda: button_click('-'), '#FF9500'),
    ('1', lambda: button_click('1'), '#505050'), ('2', lambda: button_click('2'), '#505050'), ('3', lambda: button_click('3'), '#505050'), ('+', lambda: button_click('+'), '#FF9500'),
    ('0', lambda: button_click('0'), '#505050'), ('.', lambda: button_click('.'), '#505050'), ('DEL', button_delete, '#505050'), ('=', button_equal, '#FF9500')
]

row_val = 1
col_val = 0

for (text, command, color) in buttons:
    btn = tk.Button(root, text=text, command=command, font=('Arial', 22), bg=color, fg="white", borderwidth=0)
    btn.grid(row=row_val, column=col_val, sticky='nsew', padx=5, pady=5)
    btn.configure(height=2, width=5)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
