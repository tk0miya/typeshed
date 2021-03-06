from typing import Any

class KeyFile:
    key = ...  # type: Any
    location = ...  # type: int
    closed = ...  # type: bool
    softspace = ...  # type: int
    mode = ...  # type: str
    encoding = ...  # type: str
    errors = ...  # type: str
    newlines = ...  # type: str
    name = ...  # type: Any
    def __init__(self, key) -> None: ...
    def tell(self): ...
    def seek(self, pos, whence: Any = ...): ...
    def read(self, size): ...
    def close(self): ...
    def isatty(self): ...
    def getkey(self): ...
    def write(self, buf): ...
    def fileno(self): ...
    def flush(self): ...
    def next(self): ...
    def readinto(self): ...
    def readline(self): ...
    def readlines(self): ...
    def truncate(self): ...
    def writelines(self): ...
    def xreadlines(self): ...
