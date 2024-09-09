from dataclasses import dataclass
from functools import wraps
from typing import Any, Callable, Coroutine, Union

from deflector.config.each import each
from deflector.utils.execute_function import execute


@dataclass
class Before:
    pause: Callable[[], None]
    resume: Callable[[], None]
    reset: Callable[[], None]


def before_each() -> Callable[[Callable[[], Any]], None]:
    def wrapper(func: Union[Callable[[], Coroutine[Any, Any, Any]], Callable[[], None]]) -> None:
        @wraps(func)
        def wrapped_func() -> Before:
            each.before.cb = lambda: execute(func) if each.before.status else None

            def pause() -> None:
                each.before.status = False

            def resume() -> None:
                each.before.status = True

            def reset() -> None:
                each.before.cb = None

            return Before(pause, resume, reset)

        wrapped_func()

    return wrapper
