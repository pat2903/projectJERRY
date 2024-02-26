from time import sleep

from sensor import get_ir_value
from move import move_motor_forward_timed, move_motor_forever, stop_motor
from turn import reset_steering, turn_steering, get_current_steering_motor_pos


def run_and_detect(steering_motor, motor1, motor2, ir_sensor) -> None:
    cumulative_angle = 0
    # reset steering motor before starting
    reset_steering(steering_motor)
    sleep(1)

    move_motor_forever(motor1, -500)
    move_motor_forever(motor2, -500)

    is_running = True
    while is_running:
        ir_value = get_ir_value(ir_sensor)
        print("ir: %s" % ir_value)

        if ir_value <= 10:
            reset_steering(steering_motor)
            sleep(1)
            stop_motor(motor1, action="brake")
            stop_motor(motor2, action="brake")
            is_running = False
        elif ir_value <= 50:
            print('turning')
            turn_steering(steering_motor, angle=90, speed=500)
            cumulative_angle += 90
            sleep(2)
        else:
            print(get_current_steering_motor_pos(steering_motor))
            if (cumulative_angle != 0):
                reset_steering(steering_motor)
                cumulative_angle -= 90

def run_and_detect(steering_motor, motor1, motor2, ir_sensor) -> None:
    state = "f"
    # reset steering motor before starting
    reset_steering(steering_motor)
    sleep(1)

    move_motor_forever(motor1, -500)
    move_motor_forever(motor2, -500)

    is_running = True
    while is_running:
        if get_ir_value(ir_sensor) <= 10:
            reset_steering(steering_motor)
            sleep(1)
            stop_motor(motor1, action="brake")
            stop_motor(motor2, action="brake")
            state = "s"
            is_running = False
        
        while state == "t":
            if get_ir_value(ir_sensor) > 50:
                reset_steering(steering_motor)
                state = "f"

        while state == "f":
            if get_ir_value(ir_sensor) <= 50:
                turn_steering(steering_motor, angle=90, speed=500)
                state = "t"
        

