# Pin class
class Pin:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name} (pin {self.number})"