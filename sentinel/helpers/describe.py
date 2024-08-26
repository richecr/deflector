import asyncio
import time
from functools import wraps
from typing import Any, Callable, Coroutine, Union

from sentinel import console
from sentinel.config.each import each
from sentinel.config.identation import identation


def describe(msg: str) -> Callable[[Callable[[], None]], None]:
    def wrapper(func: Union[Callable[[], Coroutine[Any, Any, None]], Callable[[], None]]) -> None:
        @wraps(func)
        def wrapped_func() -> None:
            try:
                identation.hasDescribe = True
                pre_identation = ""
                if identation.hasDescribe:
                    pre_identation += "  "
                console.print_info(f"{pre_identation}◌ {msg} › Running...")

                if each.before.cb:
                    each.before.cb()

                start = time.time_ns()
                if asyncio.iscoroutinefunction(func):
                    asyncio.run(func())
                else:
                    func()
                end = time.time_ns()

                console.print_success(
                    f"{pre_identation}✔ {msg} › Passed in {(end - start) / 1e6} ms"
                )
            except Exception as err:
                console.print_error(f"{pre_identation}✘ {msg} › Failed")
                raise err
            finally:
                identation.hasDescribe = False

                if each.after.cb:
                    each.after.cb()

        wrapped_func()

    return wrapper
