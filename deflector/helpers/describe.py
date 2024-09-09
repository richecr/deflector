import time
from functools import wraps
from typing import Any, Callable, Coroutine, Union

from deflector import console
from deflector.config.identation import identation
from deflector.utils.execute_function import execute


class Describe:
    def __call__(
        self, msg: str
    ) -> Callable[[Union[Callable[[], Coroutine[Any, Any, None]], Callable[[], None]]], None]:
        def wrapper(
            func: Union[Callable[[], Coroutine[Any, Any, None]], Callable[[], None]],
        ) -> None:
            @wraps(func)
            def wrapped_func() -> None:
                try:
                    identation.hasDescribe = True
                    pre_identation = ""
                    if identation.hasDescribe:
                        pre_identation += "  "
                    console.print_info(f"{pre_identation}◌ {msg} › Running...")

                    start = time.time_ns()
                    execute(func)
                    end = time.time_ns()

                    console.print_success(
                        f"{pre_identation}✔ {msg} › Passed in {(end - start) / 1e6} ms"
                    )
                except Exception as err:
                    console.print_error(f"{pre_identation}✘ {msg} › Failed")
                    raise err
                finally:
                    identation.hasDescribe = False

            wrapped_func()

        return wrapper

    @staticmethod
    def skip(
        msg: str,
    ) -> Callable[[Union[Callable[[], Coroutine[Any, Any, None]], Callable[[], None]]], None]:
        def wrapper(
            func: Union[Callable[[], Coroutine[Any, Any, None]], Callable[[], None]],
        ) -> None:
            @wraps(func)
            def wrapped_func() -> None:
                pre_identation = ""
                if identation.hasDescribe:
                    pre_identation += "  "
                console.print_warning(f"{pre_identation}◌ {msg} › Skipped")

            wrapped_func()

        return wrapper


describe = Describe()
