import ev3dev.ev3 as ev3

def colour_detector():
    colour_sensor = ev3.ColorSensor('in4')
    colour_sensor.mode = 'COL-COLOR'
    while(colour_sensor.color != colour_sensor.COLOR_BLUE):
        colour = colour_sensor.value()
        print(colour)
