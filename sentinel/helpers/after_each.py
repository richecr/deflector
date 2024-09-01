from functools import wraps
from typing import Any, Callable, Coroutine, Union

from sentinel.config.each import each
from sentinel.models.each import Each
from sentinel.utils.execute_function import execute


def after_each() -> Callable[[Callable[[], Any]], None]:
    def wrapper(func: Union[Callable[[], Coroutine[Any, Any, Any]], Callable[[], None]]) -> None:
        @wraps(func)
        def wrapped_func() -> Each:
            each.after.cb = lambda: execute(func) if each.after.status else None

            def pause() -> None:
                each.after.status = False

            def resume() -> None:
                each.after.status = True

            def reset() -> None:
                each.after.cb = None

            return Each(pause, resume, reset)

        wrapped_func()

    return wrapper
