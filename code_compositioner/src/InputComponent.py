from abc import ABC, abstractmethod
from typing import List

from Pin import Pin
from Component import Component

class InputComponent(Component, ABC):
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
        return f"pinMode({self.pins[0].number}, INPUT);"

    def generate_loop_code(self) -> str:
        return f"int switchState = digitalRead({self.pins[0].number});"

class Switch(InputComponent):
    pin_names = ["SWITCHPIN"]
    component_name = "Switch"
            
class RotaryEncoder(InputComponent):
    pin_names = ["PIN1", "PIN2"]
    component_name = "Rotary Encoder"
    
    def generate_pre_setup_code(self) -> str:
        return super().generate_pre_setup_code() + f"\nint {self.pins[1].name} = {self.pins[1].number};"
    
    def generate_setup_code(self) -> str:
        return f"pinMode({self.pins[0].number}, INPUT);\npinMode({self.pins[1].number}, INPUT);"

    def generate_loop_code(self) -> str:
        return f"// Logic to read rotary encoder from pins {self.pins[0].number} and {self.pins[1].number}"
    