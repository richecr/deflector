import re
from dataclasses import dataclass
from typing import Any, Callable, Coroutine, NotRequired, Optional, TypedDict


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
