from dataclasses import dataclass


@dataclass
class Identation:
    hasItOrTest: bool = False
    hasDescribe: bool = False


identation = Identation()
