#compilates code for the attiny based on sensors and outputs entered by the user

#a list of sensors and outputs
sensors = []
outputs = []

#function to add a sensor
def add_sensor():
    sensor = input("Enter the sensor: ")
    sensors.append(sensor)

#function to add an output
def add_output():
    output = input("Enter the output: ")
    outputs.append(output)


#A function that writes the base code for the attiny. Starting with a list for each line of code

#a function that writes code for an LDR sensor


#a list with the outputs of the attiny85 sparkfun board
output_pins = ["D0", "D1", "D2", "D3", "D4", "D5"]
# a dictionary with the pins of the attiny85 sparkfun board and their functions like pwm, digital, analog, etc.



# a class for the functions of the pins using type hints
class Function:
    def __init__(self, function_name: str, function_type: str):
        self.function_name = function_name
        self.function_type = function_type
        
#a class for the pins using type hints
class Pin:
    def __init__(self, pin_number: int, pin_function: Function):
        self.pin_number = pin_number
        self.pin_function = pin_function

def main():
    # TODO: Add your code here
    pass

if __name__ == "__main__":
    main()