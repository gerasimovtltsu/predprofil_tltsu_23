import tkinter as tk
from tkinter import messagebox

def calculate():
    """
    Выполняет выбранную арифметическую операцию на введенных числах и отображает результат.

    Функция получает числа и оператор из ввода пользователя, выполняет выбранную операцию и отображает результат на экране.
    Также записывает операцию и результат в историю вычислений.

    В случае ошибок (например, некорректный ввод или деление на ноль), выводит сообщение об ошибке.

    Args:
        Нет аргументов.

    Returns:
        Нет возвращаемого значения.
    """
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
    """
    Очищает историю вычислений, удаляя все записи из списка.

    Args:
        Нет аргументов.

    Returns:
        Нет возвращаемого значения.
    """
    history_listbox.delete(0, tk.END)

app = tk.Tk()
app.title("Калькулятор")

app.mainloop()