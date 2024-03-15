from turn import turn_steering, reset_steering, get_current_steering_motor_pos
from move import move_motor_forever, move_motor_forward_timed, stop_motor
from time import sleep
import ev3dev.ev3 as ev3

def canoe_turn(motorB, motorC, turn_angle, gyro: ev3.GyroSensor):
    target_angle = gyro.value() + turn_angle
    move_motor_forever(motorB, -300)
    move_motor_forever(motorC, 300)
    print("Target angle: %s", target_angle)
    while True:
        print("Current angle: %s", gyro.value())
        if gyro.value() == target_angle:
            stop_motor(motorB, "brake")
            stop_motor(motorC, "brake")
            break