from PyQt5.QtWidgets import QWidget, QHBoxLayout
from UI_ComponentBox import InputComponentBox, OutputComponentBox
from ComponentManager import ComponentManager
from UI_CodeGenerationBox import CodeGenerationBox
class MainInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QHBoxLayout()
        self.componentManager = ComponentManager()
        # Set up UI components
        self.input_handler = InputComponentBox(self)
        self.output_handler = OutputComponentBox(self)
        # self.upload_handler = UploadHandler(self.input_handler, self.output_handler)
        self.code_generation_handler = CodeGenerationBox(self)
        self.initUI()

    def initUI(self):

        self.setLayout(self.main_layout)
        self.setWindowTitle('Arduino Configurator')
        self.show()

