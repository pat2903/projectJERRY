import ev3dev.ev3 as ev3
from typing import final

colour_codes : final = {
    0: 'No colour',
    1: 'Black',
    2: 'Blue',
    3: 'Green',
    4: 'Yellow',
    5: 'Red',
    6: 'White',
    7: 'Brown'
}

def colour_detector():
    colour_sensor = ev3.ColorSensor('in4')
    colour_sensor.mode = 'COL-COLOR'
    while(colour_sensor.color != colour_sensor.COLOR_BLUE):
        colour_value = colour_sensor.value()
        print("Detected " + colour_codes[colour_value])
