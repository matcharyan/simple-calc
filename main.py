import tkinter as tk # GUI Library
from tkinter import ttk #themed widgets

def handle_button_click(button_text):
    current_expression = result_var.get() # Get display value

    if button_text == "=":
        try:
            # replace symbols with built in operators
            expression = current_expression.replace("÷", "/").replace("×", "*")
            result = eval(expression)
        
            # return int if number is whole, else keep float
            if result.is_integer():
                result = int(result)
            result_var.set(result)

        except ZeroDivisionError:
            result_var.set("Error: Division by zero")
        except Exception as e:
            result_var.set("Error: Invalid expression")

    elif button_text == "C": # Clear display
        result_var.set("")

    elif button_text == "%": # Percentage calculation
        try:
            if current_expression:
                percentage_value = float(eval(current_expression) / 100)

                result_var.set(int(percentage_value))
        except ValueError:
            result_var.set("Error")

    elif button_text == "±": # Toggle positive/negative
        try:
            number = float(current_expression) # only if not empty
            result_var.set(-number)
        except ValueError:
            result_var.set("Error")
    else: # append button text to display
        result_var.set(current_expression + button_text)

# setup main window
root = tk.Tk()
root.title("simple-calc")

# display entry widget
result_var = tk.StringVar() # store display value
result_entry = ttk.Entry(root, 
                         textvariable=result_var, 
                         font = ("Courier", 24), # monospace font
                         justify = "right") # right-align
result_entry.grid(row = 0, column = 0, columnspan = 4, sticky = "nsew")

# Button layout [text, row, column, colspan (optional)]
buttons = [
    ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
]

# Button styling
style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font = ("Courier", 24), width = 10, height = 4) # made font smaller than display

# Create and place buttons
for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    button = ttk.Button(root, 
                        text=button_text, 
                        command=lambda text=button_text: handle_button_click(text), 
                        style="TButton")
    button.grid(row=row, 
                column=col, 
                columnspan=colspan, 
                sticky="nsew", 
                ipadx=10, 
                ipady=4, 
                padx=2, 
                pady=2)

# Make rows and columns expandable
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# window size and behavior
root.geometry("400x600")
root.resizable(False, False)

# keyboard bindings
root.bind("<Return>", lambda event: handle_button_click("="))
root.bind("<BackSpace>", lambda event: handle_button_click("C"))
root.bind("<Escape>", lambda event: result_var.set(""))  # Escape key clears

# Start application
root.mainloop()
