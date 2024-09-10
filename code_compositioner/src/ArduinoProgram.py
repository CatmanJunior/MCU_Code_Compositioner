from CodeBlock import CodeBlock
from OutputComponent import OutputComponent
from InputComponent import InputComponent
from ComponentManager import ComponentManager

class ArduinoProgram:
    def __init__(self, componentManager : ComponentManager) -> None:
        self.setup_code = CodeBlock("setup")
        self.loop_code = CodeBlock("loop")
        self.componentManager = componentManager
    
    def generate_code(self):
        code = "// Auto-generated Arduino code\n#include <Arduino.h>\n"
        for component in self.componentManager.get_components():
            code += component.generate_pre_setup_code() + "\n"
        code += "\nvoid setup() {\n"
        for component in self.componentManager.get_components():
            code += component.generate_setup_code() + "\n"
        code += "}\n\nvoid loop() {\n"
        for component in self.componentManager.get_components():
            code += component.generate_loop_code() + "\n"
        code += "}\n"
        
        return code
    