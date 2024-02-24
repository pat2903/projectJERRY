#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from ev3dev2.motor import LargeMotor, MediumMotor

from detect import run_and_detect
            

def main() -> None:
    # initialise IR sensor
    ir_sensor = ev3.InfraredSensor('in1') 
    ir_sensor.mode = 'IR-PROX'

    # Initialize the motors
    steering_motor = MediumMotor('outA')
    motorB = LargeMotor('outB')
    motorC = LargeMotor('outC')

    run_and_detect(steering_motor, motorB, motorC, ir_sensor)


if __name__ == "__main__":
    main()
