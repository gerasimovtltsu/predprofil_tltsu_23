import pytest
import tkinter as tk
from PR6 import calculate, clear_history

# Создаем фикстуру для приложения
@pytest.fixture
def app():
    app = tk.Tk()
    yield app
    app.destroy()

def test_valid_addition(app):
    entry_num1 = tk.Entry(app)
    entry_num2 = tk.Entry(app)
    operator_var = tk.StringVar(app)
    operator_var.set("+")
    result_label = tk.Label(app)
    entry_num1.insert(0, "3")
    entry_num2.insert(0, "5")

    assert calculate(entry_num1.get(), entry_num2.get(), operator_var.get()) == 8.0

def test_invalid_input(app):
    entry_num1 = tk.Entry(app)
    entry_num2 = tk.Entry(app)
    operator_var = tk.StringVar(app)
    operator_var.set("+")
    result_label = tk.Label(app)
    entry_num1.insert(0, "3")
    entry_num2.insert(0, "abc")

    with pytest.raises(ValueError):
        calculate(entry_num1.get(), entry_num2.get(), operator_var.get())

def test_division_by_zero(app):
    entry_num1 = tk.Entry(app)
    entry_num2 = tk.Entry(app)
    operator_var = tk.StringVar(app)
    operator_var.set("/")
    result_label = tk.Label(app)
    entry_num1.insert(0, "5")
    entry_num2.insert(0, "0")

    with pytest.raises(tk.TclError):
        calculate(entry_num1.get(), entry_num2.get(), operator_var.get())

def test_clear_history(app):
    history_listbox = tk.Listbox(app)
    history_listbox.insert(0, "3 + 5 = 8.00")
    clear_history(history_listbox)
    assert history_listbox.size() == 0
