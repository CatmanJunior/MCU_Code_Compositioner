import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit, QHBoxLayout, QMessageBox, QListWidget
from InputComponent import InputComponent, Switch, RotaryEncoder
from OutputComponent import LED, Buzzer

class ArduinoConfigurator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.input_components = []  # Store the list of configured components
        self.output_components = []  # Store the list of configured output components
        
    def initUI(self):
        # Main horizontal layout
        main_layout = QHBoxLayout()

        # Left layout for input components
        input_layout = QVBoxLayout()
        input_layout.addWidget(QLabel('Input Components:'))


        # Dropdown to select input component
        self.component_label = QLabel('Select Input Component:')
        self.component_select = QComboBox()
        self.component_select.addItem("Switch")
        self.component_select.addItem("Rotary Encoder")
        self.component_select.currentIndexChanged.connect(self.update_input_fields)

        input_layout.addWidget(self.component_label)
        input_layout.addWidget(self.component_select)

        # Container for input fields
        self.pin_input_container = QVBoxLayout()
        self.update_input_fields()  # Initialize the first input field (Switch)
        input_layout.addLayout(self.pin_input_container)

        # Add component button
        self.add_button = QPushButton('Add Component')
        self.add_button.clicked.connect(self.add_input_component)
        input_layout.addWidget(self.add_button)

        # List widget to display added components
        self.component_list = QListWidget()
        input_layout.addWidget(self.component_list)
    
        # Upload button
        self.upload_button = QPushButton('Upload Code to Arduino')
        self.upload_button.clicked.connect(self.upload_code)
        input_layout.addWidget(self.upload_button)

        # Now create the right layout for output components
        output_layout = QVBoxLayout()
        output_layout.addWidget(QLabel('Output Components:'))

        # Dropdown to select output component (for example, LED)
        self.output_component_label = QLabel('Select Output Component:')
        self.output_component_select = QComboBox()
        self.output_component_select.addItem("LED")
        self.output_component_select.addItem("Buzzer")
        self.output_component_select.currentIndexChanged.connect(self.update_output_fields)

        output_layout.addWidget(self.output_component_label)
        output_layout.addWidget(self.output_component_select)

        # Container for output fields
        self.output_pin_container = QVBoxLayout()
        self.update_output_fields()  # Initialize with the first output component (LED)
        output_layout.addLayout(self.output_pin_container)

        # Add output component button
        self.add_output_button = QPushButton('Add Output Component')
        self.add_output_button.clicked.connect(self.add_output_component)
        output_layout.addWidget(self.add_output_button)

        # List widget to display added output components
        self.output_component_list = QListWidget()
        output_layout.addWidget(self.output_component_list)

        # Add the input and output layouts to the main horizontal layout
        main_layout.addLayout(input_layout)
        main_layout.addLayout(output_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('Arduino Configurator')
        self.show()

    def update_input_fields(self):
        """Update input fields based on the selected component."""
        # Clear existing input fields
        for i in reversed(range(self.pin_input_container.count())):
            self.pin_input_container.itemAt(i).widget().deleteLater()

        # Based on component, add appropriate pin input fields
        component = self.component_select.currentText()

        if component == "Switch":
            self.pin_label = QLabel('Pin:')
            self.pin_input = QLineEdit()
            self.pin_input.setPlaceholderText("Enter pin number")
            self.pin_input_container.addWidget(self.pin_label)
            self.pin_input_container.addWidget(self.pin_input)

        elif component == "Rotary Encoder":
            self.pinA_label = QLabel('Pin A:')
            self.pinA_input = QLineEdit()
            self.pinA_input.setPlaceholderText("Enter pin A number")
            self.pin_input_container.addWidget(self.pinA_label)
            self.pin_input_container.addWidget(self.pinA_input)

            self.pinB_label = QLabel('Pin B:')
            self.pinB_input = QLineEdit()
            self.pinB_input.setPlaceholderText("Enter pin B number")
            self.pin_input_container.addWidget(self.pinB_label)
            self.pin_input_container.addWidget(self.pinB_input)

    def add_input_component(self):
        """Add the selected component to the component list."""
        component = self.component_select.currentText()
        if component == "Switch":
            pin = self.pin_input.text()
            if pin:
                self.input_components.append(Switch(pin))
                self.component_list.addItem(f"Switch on pin {pin}")
            else:
                QMessageBox.warning(self, "Input Error", "Please enter a valid pin number for the Switch.")

        elif component == "Rotary Encoder":
            pinA = self.pinA_input.text()
            pinB = self.pinB_input.text()
            if pinA and pinB:
                self.input_components.append(RotaryEncoder(pinA, pinB))
                self.component_list.addItem(f"Rotary Encoder on pins {pinA}, {pinB}")
            else:
                QMessageBox.warning(self, "Input Error", "Please enter valid pin numbers for the Rotary Encoder.")

    def update_output_fields(self):
        """Update output fields based on the selected output component."""
        # Clear existing output fields
        for i in reversed(range(self.output_pin_container.count())):
            self.output_pin_container.itemAt(i).widget().deleteLater()

        # Based on component, add appropriate pin input fields
        component = self.output_component_select.currentText()

        if component == "LED":
            self.output_pin_label = QLabel('LED Pin:')
            self.output_pin_input = QLineEdit()
            self.output_pin_input.setPlaceholderText("Enter pin number")
            self.output_pin_container.addWidget(self.output_pin_label)
            self.output_pin_container.addWidget(self.output_pin_input)

        elif component == "Buzzer":
            self.output_pin_label = QLabel('Buzzer Pin:')
            self.output_pin_input = QLineEdit()
            self.output_pin_input.setPlaceholderText("Enter pin number")
            self.output_pin_container.addWidget(self.output_pin_label)
            self.output_pin_container.addWidget(self.output_pin_input)

    def add_output_component(self):
        """Add the selected output component to the output component list."""
        component = self.output_component_select.currentText()
        if component == "LED":
            pin = self.output_pin_input.text()
            if pin:
                self.output_components.append(LED(pin))
                self.output_component_list.addItem(f"LED on pin {pin}")
            else:
                QMessageBox.warning(self, "Input Error", "Please enter a valid pin number for the LED.")

        elif component == "Buzzer":
            pin = self.output_pin_input.text()
            if pin:
                self.output_components.append(Buzzer(pin))
                self.output_component_list.addItem(f"Buzzer on pin {pin}")
            else:
                QMessageBox.warning(self, "Input Error", "Please enter a valid pin number for the Buzzer.")


    def upload_code(self):
        """Generate code and simulate uploading it to Arduino."""
        if not self.input_components and not self.output_components:
            QMessageBox.warning(self, "No Components", "Please add at least one component before uploading.")
            return

        # Simulate code generation based on the selected components
        arduino_code = self.generate_arduino_code()
        print(arduino_code)  # For now, just print the generated code

        # Upload functionality can be added here using the ArduinoUploader class
        QMessageBox.information(self, "Upload Success", "Code generated and uploaded to Arduino (simulation).")

    def generate_arduino_code(self):
        """Generate basic Arduino code based on selected components."""
        code = "// Auto-generated Arduino code\n#include <Arduino.h>\n\nvoid setup() {\n"

        for component in self.input_components:
            code += component.generate_setup_code() + "\n"

        for component in self.output_components:
            code += component.generate_setup_code() + "\n"

        code += "}\n\nvoid loop() {\n"

        for component in self.input_components:
            code += component.generate_loop_code() + "\n"
            
        for component in self.output_components:
            code += component.generate_loop_code() + "\n"

        code += "}\n"

        return code


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ArduinoConfigurator()
    sys.exit(app.exec_())
