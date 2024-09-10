from typing import Dict
from InputComponent import *
from OutputComponent import *
from Component import *

class ComponentManager:
    def __init__(self):
        self.input_components_classes = InputComponent.__subclasses__()
        self.output_components_classes = OutputComponent.__subclasses__()

        self.component_map : Dict[str, Component] = {}
        for component in self.input_components_classes:
            self.component_map[component.component_name] = component
        for component in self.output_components_classes:
            self.component_map[component.component_name] = component
        
        self.components = {}
    
    def add_component(self, component_name: str, pins: List[int]):
        """Add a component to the list of components."""
        # Check if the component name is unique
        unique_name = False
        i=1

        while not unique_name:
            if component_name + "_" + str(i) not in self.components.keys():
                new_component_name = component_name + "_" + str(i)
                unique_name = True
            else:
                i+=1              
        print(f"Adding component {new_component_name} on pins {pins}")
        # Create the component object and add it to the dictionary of components
        component = self.component_map[component_name](component_name, pins)
        self.components[new_component_name] = component
        
    def remove_component(self, component_name: str):
        """Remove a component from the list of components."""
        if component_name in self.components.keys():
            del self.components[component_name]
        else:
            print(f"Component {component_name} not found.") 
            

    def get_components(self) -> List[Component]:
        return self.components.values()