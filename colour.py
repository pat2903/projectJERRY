COLOR_CODES = {
    0: 'No colour',
    1: 'Black',
    2: 'Blue',
    3: 'Green',
    4: 'Yellow',
    5: 'Red',
    6: 'White',
    7: 'Brown'
}

def detect_colour(colour_sensor):
    while(colour_sensor.color != colour_sensor.COLOR_BLUE):
        colour_value = colour_sensor.value()
        print("Detected " + COLOR_CODES[colour_value])
