from time import sleep

from sensor import get_ir_value
from move import move_motor_forward_timed, move_motor_forever, stop_motor
from turn import reset_steering, turn_steering, get_current_steering_motor_pos
from machine_state import MachineState


def run_and_detect(steering_motor, motor1, motor2, us_sensor) -> None:
    current_state = MachineState.RUNNING
    steering_motor.position = 0
    # reset steering motor before starting
    reset_steering(steering_motor)

    move_motor_forever(motor1, -500)
    move_motor_forever(motor2, -500)

    while current_state != MachineState.STOPPED:
        while current_state == MachineState.TURNING:
            if get_ir_value(us_sensor) <= 10:
                current_state = MachineState.STOPPED
            elif get_ir_value(us_sensor) > 50:
                reset_steering(steering_motor)
                current_state = MachineState.RUNNING

        while current_state == MachineState.RUNNING:
            if get_ir_value(us_sensor) <= 10:
                current_state = MachineState.STOPPED
            elif get_ir_value(us_sensor) <= 50:
                turn_steering(steering_motor, angle=90, speed=500)
                current_state = MachineState.TURNING
    else:
        reset_steering(steering_motor)
        sleep(1)
        stop_motor(motor1, action="brake")
        stop_motor(motor2, action="brake")