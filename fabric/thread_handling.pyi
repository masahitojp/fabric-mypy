# Stubs for fabric.thread_handling (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class ThreadHandler:
    exception = ...  # type: Any
    thread = ...  # type: Any
    def __init__(self, name, callable, *args, **kwargs) -> None: ...
    def raise_if_needed(self): ...
