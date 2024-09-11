from abc import ABC, abstractmethod
from typing import List

from Pin import Pin

# Base abstract Component class
class Component(ABC):
    pin_names : List[str] = []
    component_name : str = "Unknown Component"
    
    def __init__(self, name: str, pins: List[int]):
        self.name = name
        
        pin_names = [pin for pin in self.get_required_pin_names()]
        #generate pins dynamically
        gen_pin = []
        for i in range(len(pin_names)):
            gen_pin.append(Pin(pins[i], pin_names[i]))

        self.pins = gen_pin

    @abstractmethod
    def generate_pre_setup_code(self) -> str:
        pass

    @abstractmethod
    def generate_setup_code(self) -> str:
        pass

    @abstractmethod
    def generate_loop_code(self) -> str:
        pass
    
    @classmethod
    def get_required_pins(cls) -> int:
        return len(cls.pin_names)
    
    @classmethod
    def get_required_pin_names(cls) -> List[str]:
        return cls.pin_names

    @classmethod
    def get_component_name(cls) -> str:
        return cls.component_name