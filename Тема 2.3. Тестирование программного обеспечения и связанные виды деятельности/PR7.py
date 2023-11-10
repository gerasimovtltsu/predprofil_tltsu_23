import pytest
from unittest.mock import patch, Mock
from PR6 import calculate, clear_history

def test_addition():
    result, error_message = calculate(2, 3, "+")
    assert result == 5.0
    assert error_message is None

def test_division_by_zero():
    result, error_message = calculate(5, 0, "/")
    assert result is None
    assert error_message == "Деление на ноль невозможно"

def test_invalid_operator():
    result, error_message = calculate(5, 2, "invalid_operator")
    assert result is None
    assert error_message == "Неверный оператор"

def test_clear_history():
    history_list = ["2 + 3 = 5.00", "5 - 2 = 3.00"]
    clear_history(history_list)
    assert not history_list

if __name__ == "__main__":
    pytest.main()