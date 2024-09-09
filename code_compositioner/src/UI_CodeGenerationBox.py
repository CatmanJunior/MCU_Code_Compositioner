from PyQt5.QtWidgets import QVBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit, QListWidget, QMessageBox, QTextEdit
from ArduinoProgram import ArduinoProgram

class CodeGenerationBox:
    def __init__(self, parent) -> None:
            
        self.layout = QVBoxLayout()
        self.parent = parent
        self.component_manager = parent.componentManager
        
        self.generate_button = QPushButton('Generate Code')
        self.generate_button.clicked.connect(self.generate_code)

        # Textbox to display the generated code
        self.code_display = QTextEdit()
        self.code_display.setReadOnly(True)  # Make it read-only

        # Add button and text display to the layout
        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.code_display)
        
        
        self.parent.main_layout.addLayout(self.layout)
        
    def generate_code(self):
        """Generate Arduino code based on selected components."""
        program = ArduinoProgram(self.component_manager)
        print(self.component_manager.components)
        code = program.generate_code()
        self.code_display.setPlainText(code)
        print(code)
        # QMessageBox.information(self, 'Code Generated', 'Code generated successfully.')
        # self.parent.upload_handler.upload_code(code)