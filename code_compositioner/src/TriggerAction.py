from abc import ABC, abstractmethod

class TriggerAction(ABC):
    @abstractmethod
    def generate_code(self):
        pass
