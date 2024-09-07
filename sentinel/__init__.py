from typing import Any

from rich.console import Console

from sentinel.utils.colors import Color


class MyConsole(Console):
    def __init__(self, kwargs: dict[str, Any] = {}) -> None:
        super().__init__(**kwargs)

    def my_print(self, message: str, kwargs: dict[str, Any]) -> None:
        self.print(message, **kwargs)

    def print_error(self, message: str) -> None:
        self.print(f"[red]{message}")

    def print_success(self, message: str) -> None:
        self.print(f"[{Color.GREEN.value}]{message}")

    def print_warning(self, message: str) -> None:
        self.print(f"[yellow]{message}")

    def print_info(self, message: str) -> None:
        self.print(f"[{Color.GRAW.value}]{message}")


console = MyConsole({"color_system": "standard"})

from sentinel.modules import affirm, after_each, before_each, describe, it  # noqa: E402

__all__ = ["console", "affirm", "after_each", "before_each", "describe", "it"]
