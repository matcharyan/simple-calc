import tkinter as tk # gui
from tkinter import ttk #themed widgets

def handle_button_click(button_text):
    current_expression = result_var.get()

    if button_text == "=":
        try:
            # replace symbols with built in operators
            expression = current_expression.replace("÷", "/").replace("×", "*")
            result = eval(expression)
        
            if result.is_integer():
                result = int(result)
            
            result_var.set(result)
        except ZeroDivisionError:
            result_var.set("Error: Division by zero")
        except Exception as e:
            result_var.set("Error: Invalid expression")

    elif button_text == "C":
        result_var.set("")

    elif button_text == "%":
        try:
            if current_expression:
                percentage_value = float(eval(current_expression) / 100)

                result_var.set(int(percentage_value))
        except ValueError:
            result_var.set("Error")

    elif button_text == "±":
        try:
            number = float(current_expression)
            result_var.set(-number)
        except ValueError:
            result_var.set("Error")
    else:
        result_var.set(current_expression + button_text)

# create main window
root = tk.Tk()
root.title("simple calc")

# entry widget
result_var = tk.StringVar()
result_entry = ttk.Entry(root, textvariable=result_var, font = ("Courier", 24), justify = "right")
result_entry.grid(row = 0, column = 0, columnspan = 4, sticky = "nsew")

buttons = [
    ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
]

style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font = ("Courier", 24), width = 10, height = 4)

for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    button = ttk.Button(root, text=button_text, command=lambda text=button_text: handle_button_click(text), style="TButton")
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", ipadx=10, ipady=4, padx=5, pady=5)

for i in range(6):
    root.grid_rowconfigure(i, weight = 1)

for i in range(4):
    root.grid_columnconfigure(i, weight = 1)

width = 500
height = 700
root.geometry(f"{width}x{height}")

root.resizable(False, False)

# Keyboard control
root.bind("<Return>", lambda event: handle_button_click("="))
root.bind("<BackSpace>", lambda event: handle_button_click("C"))

# Run the main loop
root.mainloop()
