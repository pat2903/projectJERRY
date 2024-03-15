from move import move_motor_forever, stop_motor
from sensor import get_current_gyro_angle


def pivot_turn(motor1, motor2, gyro_sensor, turn_angle):
    target_angle = get_current_gyro_angle(gyro_sensor) + turn_angle

    move_motor_forever(motor1, -200)
    move_motor_forever(motor2, 200)

    # don't like this code
    while True:
        if get_current_gyro_angle(gyro_sensor) == target_angle:
            stop_motor(motor1, "brake")
            stop_motor(motor2, "brake")
            break