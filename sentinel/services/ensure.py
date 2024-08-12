import re
from dataclasses import dataclass
from typing import Any, Callable, Coroutine, NotRequired, Optional, TypedDict

from sentinel import console
from sentinel.config.identation import identation


class MyAssertionError(AssertionError):
    def __init__(
        self, expected: Any = None, actual: Any = None, message: str = "", operator: str = "=="
    ) -> None:
        self.expected = expected
        self.actual = actual
        self.message = message
        self.operator = operator
        super().__init__(message)


@dataclass
class EnsureFuncs:
    ok: Callable[[Any, str], None]
    equal: Callable[[Any, Any, str], None]
    not_equal: Callable[[Any, Any, str], None]
    match_re: Callable[[Any, str | re.Pattern[str], str], None]
    does_not_match_re: Callable[[Any, str | re.Pattern[str], str], None]
    equal_async: Optional[Callable[[Any, Any, str], Coroutine[Any, Any, None]]] = None


@dataclass
class ProcessGuaranteeOptions(TypedDict):
    message: NotRequired[str]
    default_message: NotRequired[str]
    actual: NotRequired[Any]
    expected: NotRequired[Any]
    raise_error: NotRequired[bool]
    hide_diff: NotRequired[bool]


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
        console.print_info(f"{pre_identation}  Operator {err.operator}")
        console.print_info(f"{pre_identation}  Actual:")
        console.print_error(f"{pre_identation}  {err.actual}")
        console.print_info(f"{pre_identation}  Expected:")
        console.print_success(f"{pre_identation}  {err.expected}")
        raise err


def create_ensure() -> EnsureFuncs:
    def ok(value: Any, message: str = "") -> None:
        msg = f"Operator: ==\nValue:\n{value}\nExpected:\nTrue"

        def cb() -> None:
            if not value:
                raise MyAssertionError(expected="True", actual=value, message=msg, operator="==")

        process(cb, {"message": message})

    def equal(value: Any, expected: Any, message: str = "") -> None:
        msg = f"Operator: ==\nValue:\n{value}\nExpected:\n{expected}"

        def cb() -> None:
            if value != expected:
                raise MyAssertionError(expected, value, msg, operator="==")

        process(cb, {"message": message})

    def not_equal(value: Any, expected: Any, message: str = "") -> None:
        msg = f"Operator: !=\nValue:\n{value}\nExpected:\n{expected}"

        def cb() -> None:
            if value == expected:
                raise MyAssertionError(expected, value, msg, operator="!=")

        process(cb, {"message": message})

    def match_re(value: Any, reg_exp: str | re.Pattern[str], message: str = "") -> None:
        msg = f"Operator: match_re\nValue:\n{value}\nRegExp:\n{reg_exp}"

        def cb() -> None:
            matchs = re.search(reg_exp, value)
            if not matchs:
                raise MyAssertionError(reg_exp, value, msg, operator="match_re")

        process(cb, {"message": message})

    def does_not_match_re(value: Any, reg_exp: str | re.Pattern[str], message: str = "") -> None:
        msg = f"Operator: does_not_match_re\n{value}\nRegExp:\n{reg_exp}"

        def cb() -> None:
            matchs = re.search(reg_exp, value)
            if matchs:
                raise MyAssertionError(reg_exp, value, msg, operator="does_not_match_re")

        process(cb, {"message": message})

    return EnsureFuncs(
        ok=ok,
        equal=equal,
        not_equal=not_equal,
        match_re=match_re,
        does_not_match_re=does_not_match_re,
    )
