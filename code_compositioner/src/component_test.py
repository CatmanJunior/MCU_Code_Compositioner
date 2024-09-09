from OutputComponent import LED, Buzzer
from InputComponent import Switch, RotaryEncoder, InputComponent


led = LED("LED", [13])
print(led.generate_pre_setup_code())
print(led.generate_setup_code())
print(led.generate_loop_code())

buzzer = Buzzer("Buzzer", [12])
print(buzzer.generate_pre_setup_code())
print(buzzer.generate_setup_code())
print(buzzer.generate_loop_code())

switch = Switch("Switch", [2])
print(switch.generate_setup_code())
print(switch.generate_loop_code())

rotary_encoder = RotaryEncoder("Rotary Encoder", [3, 4])
print(rotary_encoder.generate_setup_code())
print(rotary_encoder.generate_loop_code())

print(InputComponent.__subclasses__())