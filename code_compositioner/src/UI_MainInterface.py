from PyQt5.QtWidgets import QWidget, QHBoxLayout
from ComponentManager import ComponentManager
from UI_CodeGenerationBox import CodeGenerationBox
from UI_TriggerBox import TriggerBox

class MainInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QHBoxLayout()
        self.componentManager = ComponentManager()
        # Set up UI components
        from UI_ComponentBox import InputComponentBox, OutputComponentBox
        
        self.input_handler = InputComponentBox(self)
        self.output_handler = OutputComponentBox(self)
        self.trigger_handler = TriggerBox(self)
        # self.upload_handler = UploadHandler(self.input_handler, self.output_handler)
        self.code_generation_handler = CodeGenerationBox(self)
        self.initUI()

    def initUI(self):

        self.setLayout(self.main_layout)
        self.setWindowTitle('Arduino Configurator')
        self.show()
        
    def update_trigger_box(self):
        self.trigger_handler.update()

