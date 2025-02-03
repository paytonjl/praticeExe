# calculator.py
import tkinter as tk

def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.delete(0, tk.END)
            screen.insert(tk.END, result)
        except Exception as e:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Error")
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

screen = tk.Entry(root, font="Arial 20", borderwidth=2, relief="solid")
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    btn = tk.Button(root, text=button, font="Arial 15", padx=20, pady=20)
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    btn.bind("<Button-1>", button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()