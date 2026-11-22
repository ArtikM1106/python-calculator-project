import tkinter as tk


def clear():
    global first_number, operation, new_number
    first_number = 0
    operation = ""
    new_number = True
    display.set("0")
    status.set("")


def enter_digit(digit):
    global new_number
    current = "0" if new_number else display.get()
    status.set("")
    new_number = False

    if digit == ".":
        if "." not in current:
            display.set(current + ".")
    elif current == "0":
        display.set(digit)
    elif len(current) < 15:
        display.set(current + digit)


def select_operation(symbol):
    global first_number, operation, new_number
    # Если первое действие уже введено полностью, сначала получаем его результат.
    if operation and not new_number:
        if not calculate():
            return
    first_number = float(display.get())
    operation = symbol
    new_number = True
    status.set(f"{first_number:.12g} {operation}")


def calculate():
    global operation, new_number
    if not operation or new_number:
        return False

    second_number = float(display.get())
    if operation == "+":
        result = first_number + second_number
    elif operation == "−":
        result = first_number - second_number
    elif operation == "×":
        result = first_number * second_number
    elif second_number == 0:
        clear()
        status.set("На ноль делить нельзя")
        return False
    else:
        result = first_number / second_number

    status.set(f"{first_number:.12g} {operation} {second_number:.12g} =")
    display.set(f"{result:.12g}")
    operation = ""
    new_number = True
    return True


def press(symbol):
    if symbol == "C":
        clear()
    elif symbol == "=":
        calculate()
    elif symbol in ("+", "−", "×", "÷"):
        select_operation(symbol)
    else:
        enter_digit(symbol)


def create_window():
    global display, status
    window = tk.Tk()
    window.title("Калькулятор")
    window.resizable(False, False)
    window.configure(bg="#f1f5f9", padx=16, pady=16)

    display = tk.StringVar()
    status = tk.StringVar()
    clear()
    tk.Label(window, textvariable=status, anchor="e", bg="#f1f5f9",
             fg="#334155", font=("Segoe UI", 11), width=32
             ).grid(row=0, column=0, columnspan=4, sticky="ew")
    tk.Label(window, textvariable=display, anchor="e", bg="white",
             fg="#0f172a", font=("Segoe UI", 24), padx=10
             ).grid(row=1, column=0, columnspan=4, sticky="ew", pady=(4, 12))

    buttons = [
        ("7", "8", "9", "÷"),
        ("4", "5", "6", "×"),
        ("1", "2", "3", "−"),
        ("C", "0", ".", "+"),
    ]
    for row, symbols in enumerate(buttons, start=2):
        for column, symbol in enumerate(symbols):
            tk.Button(window, text=symbol, width=5, font=("Segoe UI", 14),
                      command=lambda value=symbol: press(value)
                      ).grid(row=row, column=column, padx=2, pady=2, sticky="ew")

    tk.Button(window, text="=", font=("Segoe UI", 14), bg="#2458a6", fg="white",
              command=calculate
              ).grid(row=6, column=0, columnspan=4, sticky="ew", padx=2, pady=(5, 0))
    return window


if __name__ == "__main__":
    create_window().mainloop()

