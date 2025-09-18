from machine import Pin
from neopixel import NeoPixel
import time 

power = Pin(2, Pin.OUT)
power.value(1)

pin = Pin(0, Pin.OUT)
np = NeoPixel(pin, 1)

button = Pin(38, Pin.IN, Pin.PULL_UP)

def show_color(r, g, b):
    np[0] = (r, g, b)
    np.write()
    
press_count = 0
was_down = False

while True:
    if button.value() == 0:  
        show_color(0, 255, 0)  # green
        was_down = True
    else:  # released
        if was_down:
            press_count += 1
            was_down = False
            if press_count >= 5:
                show_color(0, 0, 0)  # off
                print("You have successfully implemented LAB1!")
                break
        else:
            show_color(255, 0, 0) 
    time.sleep(0.02)  