from CodeBlock import CodeBlock

class ArduinoProgram:
    def __init__(self):
        self.setup_code = CodeBlock("setup")
        self.loop_code = CodeBlock("loop")
        self.input_components = []
        self.trigger_actions = []
    
    def add_input_component(self, input_component):
        self.input_components.append(input_component)
    
    def add_trigger_action(self, trigger_action):
        self.trigger_actions.append(trigger_action)
    
    def generate_code(self):
        code = "// Auto-generated Arduino code\n"
        code += "#include <Arduino.h>\n\n"
        
        # Setup code
        code += "void setup() {\n"
        code += self.setup_code.generate_code() + "\n"
        code += "}\n\n"
        
        # Loop code
        code += "void loop() {\n"
        code += self.loop_code.generate_code() + "\n"
        code += "}\n\n"
        
        return code
