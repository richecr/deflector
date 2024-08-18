import inspect


def get_caller() -> tuple[str | None, int | None]:
    stack = inspect.stack()
    for frame in stack:
        if "sentinel/sentinel" not in frame.filename:
            filename = frame.filename
            line = frame.lineno
            return filename, line

    return None, None
