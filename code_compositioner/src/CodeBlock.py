from typing import List
class CodeBlock:
    def __init__(self, block_name: str):
        self.block_name = block_name
        self.code_lines:List[str] = []
    
    def add_line(self, line: str):
        self.code_lines.append(line)
    
    def generate_code(self):
        return "\n".join(self.code_lines)