from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class EachConfigs:
    status: bool
    cb: Optional[Callable[[], None]]


@dataclass
class Each:
    before: EachConfigs
    after: EachConfigs


each = Each(before=EachConfigs(status=True, cb=None), after=EachConfigs(status=True, cb=None))
