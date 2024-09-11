from PyQt5.QtWidgets import QVBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit, QListWidget, QMessageBox, QWidget
from Component import Component
from ComponentManager import ComponentManager
from UI_MainInterface import MainInterface

class ComponentBox:
    def __init__(self, parent : MainInterface , component_type) -> None:
        self.parent = parent
        self.component_type = component_type  # "input" or "output"
        self.components : list[Component] = []
        self.component_manager : ComponentManager = parent.componentManager  
        if self.component_type == "input":
            componentlist = self.component_manager.input_components_classes
        else:
            componentlist = self.component_manager.output_components_classes

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel(f'{self.component_type.capitalize()} Components:'))

        # Dropdown to select component
        self.component_label = QLabel(f'Select {self.component_type.capitalize()} Component:')
        self.component_select = QComboBox()
        for comp in componentlist:
            self.component_select.addItem(comp.get_component_name())
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

    def update_fields(self) -> None:
        """Update input fields based on the selected component."""
        # Clear existing input fields
        for i in reversed(range(self.pin_input_container.count())):
            if (item := self.pin_input_container.itemAt(i)) is not None and (widget := item.widget()) is not None:
                widget.deleteLater()


        # Get the selected component
        component_class: Component = self.component_manager.get_component_class(self.component_select.currentText())
        # Ensure the component_class is valid
        if component_class is None:
            QMessageBox.warning(self.parent, "Component Error", "Selected component class not found.")
            return

        if not issubclass(component_class, Component):
            QMessageBox.warning(self.parent, "Component Error", "Selected class is not a valid Component subclass.")
            return

        # Instantiate the component class
        component: Component = component_class("", [])
        
        # Update fields based on the selected component
        for pin in component.get_required_pin_names():
            pin_label = QLabel(f"{pin}:")
            pin_input = QLineEdit()
            pin_input.setPlaceholderText(f"Enter pin number for {pin}")
            self.pin_input_container.addWidget(pin_label)
            self.pin_input_container.addWidget(pin_input)

    def add_component(self) -> None:
        """Add the selected component to the list."""
        # Get the selected component
        component_name = self.component_select.currentText()
        component_class: type[Component] = self.component_manager.component_map[component_name]

        # Gather pin inputs
        pin_numbers = []
        for i in range(self.pin_input_container.count()):
            if (item := self.pin_input_container.itemAt(i)) is not None and (widget := item.widget()) is not None:
                pin_number_str = widget.text()
                if pin_number_str.isdigit():
                    pin_numbers.append(int(pin_number_str))
                else:
                    QMessageBox.warning(self.parent, "Input Error", "Please enter valid pin numbers.")
                    return

        # Validate the pin count and add the component
        required_pins = component_class.get_required_pin_names()
        component : Component = component_class(component_name, pin_numbers)
        if len(pin_numbers) == len(required_pins):
            self.components.append(component)
            self.component_list.addItem(f"{component_name} on pins {', '.join(map(str, pin_numbers))}")
            self.component_manager.add_component(component_name, pin_numbers)
            self.parent.update_trigger_box()
        else:
            QMessageBox.warning(self.parent, "Input Error", f"{component_name} requires exactly {len(required_pins)} pin(s).")


class InputComponentBox(ComponentBox):
    def __init__(self, parent):
        super().__init__(parent, component_type="input")


class OutputComponentBox(ComponentBox):
    def __init__(self, parent):
        super().__init__(parent, component_type="output")