from .typing import Duck


def create_duck(name: str) -> Duck:
    class Ducky:
        def __init__(self):
            self.name = name

        def walk(self) -> None:
            print(self.name, "is walking")

        def quack(self) -> None:
            print(self.name, "says 'quack'")

    return Ducky()
