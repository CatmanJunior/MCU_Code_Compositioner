from abc import ABC, abstractmethod
from typing import List

from Pin import Pin
from Component import Component

# OutputComponent abstract class inheriting from Component
class OutputComponent(Component, ABC):
    def __init__(self, name: str, pins: List[int]):
        pin_names = [pin for pin in self.get_required_pin_names()]
        #generate pins dynamically
        gen_pin = []
        for i in range(len(pin_names)):
            gen_pin.append(Pin(pins[i], pin_names[i]))
        super().__init__(name, gen_pin)

    def generate_pre_setup_code(self) -> str:
        return f"int {self.pins[0].name} = {self.pins[0].number};"  # Define the LED pin number

    def generate_setup_code(self) -> str:
        return f"pinMode({self.pins[0].name}, OUTPUT);"

    def generate_loop_code(self) -> str:
        return f"digitalWrite({self.pins[0].name}, HIGH);"

class LED(OutputComponent):
    pin_names = ["LEDPIN"]
    component_name = "LED"

class Buzzer(OutputComponent):
    pin_names = ["BUZZERPIN"]
    component_name = "Buzzer"