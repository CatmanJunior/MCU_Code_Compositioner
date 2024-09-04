from abc import ABC, abstractmethod
from typing import List

from Pin import Pin
from Component import Component

# OutputComponent abstract class inheriting from Component
class OutputComponent(Component, ABC):
    def __init__(self, name: str, pins: List[Pin]):
        super().__init__(name, pins)



class LED(OutputComponent):
    def __init__(self, pins: List[Pin]):
        super().__init__("LED", pins)
    
    def generate_setup_code(self) -> str:
        return f"pinMode({self.pins[0].number}, OUTPUT);"

    def generate_loop_code(self) -> str:
        return f"digitalWrite({self.pins[0].number}, HIGH);  // Turn on the LED"


# Concrete Buzzer class
class Buzzer(OutputComponent):
    def __init__(self, pins: List[Pin]):
        super().__init__("Buzzer", pins)

    def generate_setup_code(self) -> str:
        return f"pinMode({self.pins[0].number}, OUTPUT);"

    def generate_loop_code(self) -> str:
        return f"digitalWrite({self.pins[0].number}, HIGH);  // Activate the buzzer"