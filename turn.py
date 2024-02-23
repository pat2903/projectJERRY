#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent
from time import sleep

# Initialize the motors.
motorB = LargeMotor('outB')
motorC = LargeMotor('outC')
steering_motor = MediumMotor('outA')

steering_motor.run_to_abs_pos(position_sp=0, speed_sp=500)

# To run both motors at the same speed.
motorB.run_forever(speed_sp=-500)
motorC.run_forever(speed_sp=-500)

sleep(1)

# positive angle turns left
steering_motor.run_to_rel_pos(position_sp=90, speed_sp=500)

sleep(1)

steering_motor.run_to_rel_pos(position_sp=-90, speed_sp=500)

sleep(1)

motorB.stop(stop_action="coast")
motorC.stop(stop_action="coast")

# # To straighten the wheel, turn it 45 degrees to the right.
# steering_motor.run_to_rel_pos(position_sp=-90, speed_sp=500)

steering_motor.run_to_abs_pos(position_sp=0, speed_sp=500)

steering_motor.stop(stop_action="coast")