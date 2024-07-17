from typing import Protocol


class Duck(Protocol):
    def walk(self) -> None:
        ...

    def quack(self) -> None:
        ...
