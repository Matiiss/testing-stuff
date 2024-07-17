from typing import Protocol, runtime_checkable


@runtime_checkable
class Duck(Protocol):
    name: str

    def walk(self) -> None: ...

    def quack(self) -> None: ...
