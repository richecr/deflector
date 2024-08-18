from typing import Any


class MyAssertionError(AssertionError):
    def __init__(self, expected: Any = None, actual: Any = None, operator: str = "==") -> None:
        self.expected = expected
        self.actual = actual
        self.operator = operator
        super().__init__(f"Operator: {operator}\nActual:\n{actual}\Expected:\n{expected}")
