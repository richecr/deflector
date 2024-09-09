import asyncio
from typing import Any, Callable, Coroutine, Union


def execute(func: Union[Callable[[], Coroutine[Any, Any, None]], Callable[[], None]]) -> None:
    if asyncio.iscoroutinefunction(func):
        asyncio.run(func())
    else:
        func()
