from time import sleep

from sensor import get_ir_value
from move import move_motor_forward_timed, move_motor_forever, stop_motor
from turn import reset_steering, turn_steering, get_current_steering_motor_pos


def run_and_detect(steering_motor, motor1, motor2, ir_sensor) -> None:
    reset_range = [x for x in range(-10, 11)]
    # reset steering motor before starting
    reset_steering(steering_motor)
    sleep(1)

    is_running = True
    while is_running:
        ir_value = get_ir_value(ir_sensor)

        if ir_value <= 10:
            reset_steering(steering_motor)
            sleep(1)
            stop_motor(motor1, action="brake")
            stop_motor(motor2, action="brake")
            is_running = False
        elif ir_value <= 50:
            turn_steering(steering_motor, angle=90, speed=500)
        else:
            if (get_current_steering_motor_pos(steering_motor) not in reset_range):
                print(get_current_steering_motor_pos(steering_motor))
                reset_steering(steering_motor)
            move_motor_forever(motor1, -500)
            move_motor_forever(motor2, -500)
