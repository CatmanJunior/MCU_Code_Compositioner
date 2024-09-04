from abc import ABC, abstractmethod
from typing import List
from Pin import Pin

# Base abstract Component class
class Component(ABC):
    def __init__(self, name: str, pins: List[Pin]):
        self.name = name
        self.pins = pins

    @abstractmethod
    def generate_setup_code(self) -> str:
        pass

    @abstractmethod
    def generate_loop_code(self) -> str:
        pass