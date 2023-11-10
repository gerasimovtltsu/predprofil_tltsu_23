import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                messagebox.showerror("Ошибка", "Деление на ноль невозможно")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Ошибка", "Неверный оператор")
            return

        result_label.config(text=f"Результат: {result}")
        history_listbox.insert(0, f"{num1} {operator} {num2} = {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числа")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

def clear_history():
    history_listbox.delete(0, tk.END)

app = tk.Tk()
app.title("Калькулятор")

entry_num1 = tk.Entry(app, width=10)
entry_num1.grid(row=0, column=0)

operator_var = tk.StringVar(app)
operator_var.set("+")  # Устанавливаем оператор по умолчанию

operator_menu = tk.OptionMenu(app, operator_var, "+", "-", "*", "/")
operator_menu.grid(row=0, column=1)

entry_num2 = tk.Entry(app, width=10)
entry_num2.grid(row=0, column=2)

calculate_button = tk.Button(app, text="Вычислить", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3)

result_label = tk.Label(app, text="Результат: ")
result_label.grid(row=2, column=0, columnspan=3)

history_listbox = tk.Listbox(app, width=40, height=5)
history_listbox.grid(row=3, column=0, columnspan=3)

clear_button = tk.Button(app, text="Очистить историю", command=clear_history)
clear_button.grid(row=4, column=0, columnspan=3)

app.mainloop()