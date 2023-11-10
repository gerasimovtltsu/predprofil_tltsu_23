import unittest
import tkinter as tk
from PR6 import calculate, clear_history

"""
Запуск тестов:
python -m unittest PR6_test.TestCalculator.test_valid_subtraction

вместо test_valid_subtraction подставь названия функций
"""

class TestCalculatorApp(unittest.TestCase):
    def setUp(self):
        self.app = tk.Tk()
        self.entry_num1 = tk.Entry(self.app, width=10)
        self.operator_var = tk.StringVar(self.app)
        self.operator_var.set("+")
        self.entry_num2 = tk.Entry(self.app, width=10)
        self.result_label = tk.Label(self.app, text="Результат: ")
        self.history_listbox = tk.Listbox(self.app, width=40, height=5)

    def test_valid_addition(self):
        # Ваш тест для сложения
        self.entry_num1.insert(0, "3")
        self.entry_num2.insert(0, "5")
        self.operator_var.set("+")
        calculate(self.entry_num1.get(), self.entry_num2.get(), self.operator_var.get())
        # Далее добавьте проверку результата

    def test_invalid_input(self):
        # Ваш тест для некорректного ввода
        self.entry_num1.insert(0, "3")
        self.entry_num2.insert(0, "abc")
        self.operator_var.set("+")
        with self.assertRaises(ValueError):
            calculate(self.entry_num1.get(), self.entry_num2.get(), self.operator_var.get())

    def test_division_by_zero(self):
        # Проверка деления на ноль
        self.entry_num1.insert(0, "5")
        self.entry_num2.insert(0, "0")
        self.operator_var.set("/")
        with self.assertRaises(tk.TclError) as context:
            calculate(self.entry_num1.get(), self.entry_num2.get(), self.operator_var.get())
        self.assertEqual(str(context.exception), "Деление на ноль невозможно")

    def test_valid_subtraction(self):
        # Ваш тест для вычитания
        self.entry_num1.insert(0, "10")
        self.entry_num2.insert(0, "3")
        self.operator_var.set("-")
        calculate(self.entry_num1.get(), self.entry_num2.get(), self.operator_var.get())
        # Далее добавьте проверку результата

if __name__ == "__main__":
    unittest.main()