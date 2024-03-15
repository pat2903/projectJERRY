def get_ir_value(ir_sensor) -> int:
    return ir_sensor.value()

def get_current_gyro_angle(gyro_sensor) -> int:
    return gyro_sensor.value()

def get_colour_sensor_value(colour_sensor) -> int:
    return colour_sensor.value()