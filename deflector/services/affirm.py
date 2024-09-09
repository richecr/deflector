import re
from typing import Any, Callable

from deflector import console
from deflector.config.identation import identation
from deflector.models.affirm import AffirmFuncs, ProcessGuaranteeOptions
from deflector.models.assertion import MyAssertionError
from deflector.utils.errors import get_caller


def process(func: Callable[[], None], options: ProcessGuaranteeOptions) -> None:
    pre_identation = ""
    if identation.hasDescribe:
        pre_identation += "  "
    if identation.hasItOrTest:
        pre_identation += "    "
    if not pre_identation:
        pre_identation = "  "

    try:
        func()
        if options.get("message"):
            console.print_success(f"{pre_identation}✔ {options['message']}")

    except MyAssertionError as err:
        console.print_error(f"{pre_identation}✘ {options['message']}")
        file, line = get_caller()
        if line and file:
            console.print_info(f"{pre_identation}  File {file}, line {line}")

        console.print_info(f"{pre_identation}  Operator {err.operator}")
        console.print_info(f"{pre_identation}  Actual:")
        console.print_error(f"{pre_identation}  {err.actual}")

        if "match_re" in err.operator:
            console.print_info(f"{pre_identation}  RegExp:")
        else:
            console.print_info(f"{pre_identation}  Expected:")
        console.print_success(f"{pre_identation}  {err.expected}")

        raise err


def create_affirm() -> AffirmFuncs:
    def ok(value: Any, message: str = "") -> None:
        def cb() -> None:
            if not value:
                raise MyAssertionError(expected="True", actual=value, operator="==")

        process(cb, {"message": message})

    def equal(value: Any, expected: Any, message: str = "") -> None:
        def cb() -> None:
            if value != expected:
                raise MyAssertionError(expected, value, operator="==")

        process(cb, {"message": message})

    def not_equal(value: Any, expected: Any, message: str = "") -> None:
        def cb() -> None:
            if value == expected:
                raise MyAssertionError(expected, value, operator="!=")

        process(cb, {"message": message})

    def match_re(value: Any, reg_exp: str | re.Pattern[str], message: str = "") -> None:
        def cb() -> None:
            matchs = re.search(reg_exp, value)
            if not matchs:
                raise MyAssertionError(reg_exp, value, operator="match_re")

        process(cb, {"message": message})

    def does_not_match_re(value: Any, reg_exp: str | re.Pattern[str], message: str = "") -> None:
        def cb() -> None:
            matchs = re.search(reg_exp, value)
            if matchs:
                raise MyAssertionError(reg_exp, value, operator="does_not_match_re")

        process(cb, {"message": message})

    return AffirmFuncs(
        ok=ok,
        equal=equal,
        not_equal=not_equal,
        match_re=match_re,
        does_not_match_re=does_not_match_re,
    )
