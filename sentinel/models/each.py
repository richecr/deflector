from dataclasses import dataclass
from typing import Callable


@dataclass
class Each:
    pause: Callable[[], None]
    resume: Callable[[], None]
    reset: Callable[[], None]
