from PyQt5.QtWidgets import QVBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit, QListWidget, QMessageBox
from Component import Component

class ComponentBox:
    def __init__(self, parent, component_type):
        self.parent = parent
        self.component_type = component_type  # "input" or "output"
        self.components = []
        self.component_manager = parent.componentManager  
        componentlist = self.component_manager.component_map.keys()

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel(f'{self.component_type.capitalize()} Components:'))

        # Dropdown to select component
        self.component_label = QLabel(f'Select {self.component_type.capitalize()} Component:')
        self.component_select = QComboBox()
        for comp in componentlist:
            self.component_select.addItem(comp)
        self.component_select.currentIndexChanged.connect(self.update_fields)

        self.layout.addWidget(self.component_label)
        self.layout.addWidget(self.component_select)

        # Container for pin input fields
        self.pin_input_container = QVBoxLayout()
        self.update_fields()  # Initialize with the first component
        self.layout.addLayout(self.pin_input_container)

        # Add component button
        self.add_button = QPushButton(f'Add {self.component_type.capitalize()} Component')
        self.add_button.clicked.connect(self.add_component)
        self.layout.addWidget(self.add_button)

        # List widget to display added components
        self.component_list = QListWidget()
        self.layout.addWidget(self.component_list)

        # Add the layout to the parent's main layout
        parent.main_layout.addLayout(self.layout)

    def update_fields(self):
        """Update input fields based on the selected component."""
        # Clear existing input fields
        for i in reversed(range(self.pin_input_container.count())):
            self.pin_input_container.itemAt(i).widget().deleteLater()

        # Get the selected component
        component: Component = self.component_manager.component_map[self.component_select.currentText()]

        # Update fields based on the selected component
        for pin in component.get_required_pin_names():
            pin_label = QLabel(f"{pin}:")
            pin_input = QLineEdit()
            pin_input.setPlaceholderText(f"Enter pin number for {pin}")
            self.pin_input_container.addWidget(pin_label)
            self.pin_input_container.addWidget(pin_input)

    def add_component(self):
        """Add the selected component to the list."""
        # Get the selected component
        component_name = self.component_select.currentText()
        component: Component = self.component_manager.component_map[component_name]

        # Gather pin inputs
        pin_numbers = []
        for i in range(self.pin_input_container.count()):
            widget = self.pin_input_container.itemAt(i).widget()
            if isinstance(widget, QLineEdit):
                pin_number_str = widget.text()
                if pin_number_str.isdigit():
                    pin_numbers.append(int(pin_number_str))
                else:
                    QMessageBox.warning(self.parent, "Input Error", "Please enter valid pin numbers.")
                    return

        # Validate the pin count and add the component
        required_pins = component.get_required_pin_names()
        if len(pin_numbers) == len(required_pins):
            self.components.append(component)
            self.component_list.addItem(f"{component_name} on pins {', '.join(map(str, pin_numbers))}")
            self.component_manager.add_component(component_name, pin_numbers)
        else:
            QMessageBox.warning(self.parent, "Input Error", f"{component_name} requires exactly {len(required_pins)} pin(s).")


class InputComponentBox(ComponentBox):
    def __init__(self, parent):
        super().__init__(parent, component_type="input")


class OutputComponentBox(ComponentBox):
    def __init__(self, parent):
        super().__init__(parent, component_type="output")