from abc import ABC, abstractmethod
from typing import List

from Pin import Pin

# Base abstract Component class
class Component(ABC):
    def __init__(self, name: str, pins: List[Pin]):
        self.name = name
        self.pins = pins

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
        return cls.pin_names.count  # LED requires 1 pin
    
    @classmethod
    def get_required_pin_names(cls) -> List[str]:
        return cls.pin_names

    @classmethod
    def get_component_name(cls) -> str:
        return cls.component_name