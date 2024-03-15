#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from ev3dev2.motor import LargeMotor
from time import sleep

from detect import run_and_detect
from pivot_turn import pivot_turn
from colour import detect_colour
            

def main() -> None:
    # initialize the motors
    motorB = LargeMotor('outB')
    motorC = LargeMotor('outC')

    # initialise gyro sensor
    gyro_sensor = ev3.GyroSensor('in4')
    
    # reset gyro angle to 0
    gyro_sensor.mode = 'GYRO-RATE'
    gyro_sensor.mode = 'GYRO-ANG'

    # initialise colour sensor
    colour_sensor = ev3.ColorSensor('in4')
    colour_sensor.mode = 'COL-COLOR'

    # initialise US sensor
    # us_sensor = ev3.UltrasonicSensor('in2') 
    # us_sensor.mode = 'US-DIST-CM'

    pivot_turn(motorB, motorC, gyro_sensor, 90)

    # run_and_detect(steering_motor, motorB, motorC, us_sensor)


if __name__ == "__main__":
    main()
