#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from ev3dev2.motor import LargeMotor, MediumMotor

from detect import run_and_detect
from canoe_turn import canoe_turn
from move import move_motor_forward_timed
from turn import turn_steering
from colour import colour_detector
            

def main() -> None:
    # initialise IR sensor
    ir_sensor = ev3.InfraredSensor('in1') 
    ir_sensor.mode = 'IR-PROX'

    # Initialize the motors
    steering_motor = MediumMotor('outA')
    motorB = LargeMotor('outB')
    motorC = LargeMotor('outC')

    # run_and_detect(steering_motor, motorB, motorC, ir_sensor)
    # canoe_turn(steering_motor, motorB, motorC)

    # turn_steering(steering_motor, -90, 100)
    # move_motor_forward_timed(motorB, 5000, -400)
    # move_motor_forward_timed(motorC, 5000, -400)
    colour_detector()
    


if __name__ == "__main__":
    main()
