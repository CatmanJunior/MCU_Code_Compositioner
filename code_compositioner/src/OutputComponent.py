from abc import ABC, abstractmethod
from typing import Dict, List

from Pin import Pin
from Component import Component

# OutputComponent abstract class inheriting from Component
class OutputComponent(Component, ABC):
    states : Dict[str,str]= {}
    def __init__(self, name: str, pins: List[int]):
        super().__init__(name, pins)

    def generate_pre_setup_code(self) -> str:
        return f"int {self.pins[0].name} = {self.pins[0].number};"  # Define the LED pin number

    def generate_setup_code(self) -> str:
        return f"pinMode({self.pins[0].name}, OUTPUT);"

    def generate_loop_code(self) -> str:
        return f"digitalWrite({self.pins[0].name}, HIGH);"

    @classmethod
    def get_states(cls) -> List[str]:
        return list(cls.states.keys())

class LED(OutputComponent):
    pin_names = ["LEDPIN"]
    component_name = "LED"
    states = {
        'ON': 'HIGH',
        'OFF': 'LOW'
    }
    
class Buzzer(OutputComponent):
    pin_names = ["BUZZERPIN"]
    component_name = "Buzzer"
    states = {
        'C': '262',
        'D': '294',
        'E': '330',
        'F': '349'
    }