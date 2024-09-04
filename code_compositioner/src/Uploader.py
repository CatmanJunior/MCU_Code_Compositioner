import subprocess

class ArduinoUploader:
    def __init__(self, arduino_path):
        self.arduino_path = arduino_path  # Path to Arduino CLI or IDE
    
    def upload(self, code):
        with open("generated_code.ino", "w") as code_file:
            code_file.write(code)
        
        # Assuming using Arduino CLI to compile and upload the code
        subprocess.run([self.arduino_path, "--upload", "generated_code.ino"])
