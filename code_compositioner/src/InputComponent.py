from abc import ABC, abstractmethod
from typing import List

from Pin import Pin
from Component import Component

class InputComponent(Component, ABC):
    def __init__(self, name: str, pins: List[Pin]):
        super().__init__(name, pins)

    @abstractmethod
    def generate_setup_code(self):
        pass

    @abstractmethod
    def generate_loop_code(self):
        pass
    
class Switch(InputComponent):
    def generate_setup_code(self) -> str:
        return f"pinMode({self.pins[0].number}, INPUT);"

    def generate_loop_code(self) -> str:
        return f"int switchState = digitalRead({self.pins[0].number});"
    
class RotaryEncoder(InputComponent):
    def generate_setup_code(self) -> str:
        return f"pinMode({self.pins[0].number}, INPUT);\npinMode({self.pins[1].number}, INPUT);"

    def generate_loop_code(self) -> str:
        return f"// Logic to read rotary encoder from pins {self.pins[0].number} and {self.pins[1].number}"
