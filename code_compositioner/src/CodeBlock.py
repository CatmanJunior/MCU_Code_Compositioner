class CodeBlock:
    def __init__(self, block_name):
        self.block_name = block_name
        self.code_lines = []
    
    def add_line(self, line):
        self.code_lines.append(line)
    
    def generate_code(self):
        return "\n".join(self.code_lines)