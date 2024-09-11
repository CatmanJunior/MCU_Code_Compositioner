from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QHBoxLayout
from InputComponent import InputComponent
from OutputComponent import OutputComponent

class TriggerBox():
    def __init__(self, parent):
        self.layout = QVBoxLayout()
        self.parent = parent
        # Dropdown for selecting input component
        self.input_select_label = QLabel("Select Input Component:")
        self.input_select = QComboBox()
        self.input_select.addItems([comp.name for comp in parent.componentManager.get_components() if isinstance(comp, InputComponent)])
        

        
        # Dropdown for selecting output component
        self.output_select_label = QLabel("Select Output Component:")
        self.output_select = QComboBox()
        self.output_select.addItems([comp.name for comp in parent.componentManager.get_components() if isinstance(comp, OutputComponent)])
        self.output_select.currentIndexChanged.connect(self.update_output_states)  # Connect to state update

        # Dropdown for selecting output state
        self.state_select_label = QLabel("Select Output State:")
        self.state_select = QComboBox()
        
        # Button to confirm trigger connection
        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_trigger)
        
        # Layout setup
        self.layout.addWidget(self.input_select_label)
        self.layout.addWidget(self.input_select)
        self.layout.addWidget(self.state_select_label)
        self.layout.addWidget(self.state_select)
        self.layout.addWidget(self.output_select_label)
        self.layout.addWidget(self.output_select)
        self.layout.addWidget(self.connect_button)
        
        self.parent.main_layout.addLayout(self.layout)
        
    def update_output_states(self):
        """Update the output states dropdown based on the selected output component."""
        selected_output = self.output_select.currentText()
        self.state_select.clear()
        self.state_select.addItems(self.parent.componentManager.component_map[selected_output].get_states())

    
    def connect_trigger(self):
        # Logic for connecting the input, state, and output
        input_component = self.input_select.currentText()
        state = self.state_select.currentText()
        output_component = self.output_select.currentText()
        
        print(f"Connected {input_component} ({state}) to {output_component}")
        # Add your trigger logic here
    
    def update(self):
        # Update the dropdowns with the current components
        self.input_select.clear()
        self.input_select.addItems([comp.name for comp in self.parent.componentManager.get_components() if isinstance(comp, InputComponent)])
        current_output = self.output_select.currentText
        self.output_select.clear()
        self.output_select.addItems([comp.name for comp in self.parent.componentManager.get_components() if isinstance(comp, OutputComponent)])
        self.output_select.currentText= current_output