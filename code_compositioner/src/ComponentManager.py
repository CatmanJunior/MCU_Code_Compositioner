from typing import Dict
from InputComponent import *
from OutputComponent import *
from Component import *

class ComponentManager:
    def __init__(self) -> None:
        self.input_components_classes  = InputComponent.__subclasses__()
        self.output_components_classes = OutputComponent.__subclasses__()

        self.__component_map : Dict[str, type[Component]] = {}
        
        for i_component in self.input_components_classes:
            self.__component_map[i_component.component_name] = i_component
            
        for o_component in self.output_components_classes:
            self.__component_map[o_component.component_name] = o_component
        
        self.__components : Dict[str,Component] = {}
    
    def add_component(self, component_name: str, pins: List[int]) -> Component:
        """Add a component to the list of components."""
        # Check if the component name is unique
        unique_name = False
        i=1

        while not unique_name:
            if component_name + "_" + str(i) not in self.__components.keys():
                new_component_name = component_name + "_" + str(i)
                unique_name = True
            else:
                i+=1              
        print(f"Adding component {new_component_name} on pins {pins}")
        # Create the component object and add it to the dictionary of components
        componentClass = self.get_component_class(component_name)
        
        new_component = componentClass(new_component_name, pins)
        self.__components[new_component_name] = new_component
        return new_component
        
    def remove_component(self, component_name: str):
        """Remove a component from the list of components."""
        if component_name in self.__components.keys():
            del self.__components[component_name]
        else:
            print(f"Component {component_name} not found.") 
            
    def get_component_class(self, component_name: str) -> type[Component]:
        return self.__component_map[component_name]

    def get_components(self) -> List[Component]:
        return list(self.__components.values())
    