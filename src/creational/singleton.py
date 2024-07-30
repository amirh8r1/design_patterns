"""
    Singletone
        -Ensure a class only has one instance,
        and provide a global point of access to it.
"""


# First implementation
from typing import Any


class A:
    _instance = None

    def __init__(self) -> None:
        raise RuntimeError("call get_instance()")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


# Second implementation
class Singleton(type):
    _instance = None

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class B(metaclass=Singleton):
    pass
