import time
from typing import Callable

from sentinel import console
from sentinel.config.each import each
from sentinel.config.identation import identation


def describe(msg: str, func: Callable[[], None]) -> None:
    try:
        identation.hasDescribe = True
        pre_identation = ""
        if identation.hasDescribe:
            pre_identation += "  "
        console.print_info(f"{pre_identation}◌ {msg} › Running...")

        if each.before.cb:
            each.before.cb()

        start = time.time_ns()
        func()
        end = time.time_ns()

        console.print_success(f"{pre_identation}✔ {msg} › Passed in {end - start}ns")
    except Exception as err:
        console.print_error(f"{pre_identation}✘ {msg} › Failed")
        raise err
    finally:
        identation.hasDescribe = False

        if each.after.cb:
            each.after.cb()
