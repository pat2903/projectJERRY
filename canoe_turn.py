from turn import turn_steering, reset_steering, get_current_steering_motor_pos
from move import move_motor_forever, move_motor_forward_timed, stop_motor
from time import sleep

def canoe_turn(steering_motor, motorB, motorC):
    turn_steering(steering_motor, -90,  100)
    sleep(2)
    move_motor_forward_timed(motorB, 5000, -400)
    move_motor_forward_timed(motorC, 5000, 600)
    sleep(2)
    reset_steering(steering_motor)