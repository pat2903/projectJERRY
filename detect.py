#!/usr/bin/env python3 


import ev3dev.ev3 as ev3 
from time import sleep
from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent


# Initialize the motors.
motorB = LargeMotor('outB')
motorC = LargeMotor('outC')
steering_motor = MediumMotor('outA')

ir = ev3.InfraredSensor('in1') 
ir.mode = 'IR-PROX' 

def getIRValue():
    return ir.value()

def moveForward():
    steering_motor.run_to_abs_pos(position_sp=0, speed_sp=500)

    # To run both motors at the same speed.
    motorB.run_forever(speed_sp=-500)
    motorC.run_forever(speed_sp=-500)

def stop():
    steering_motor.run_to_abs_pos(position_sp=0, speed_sp=500)
    sleep(0.5)
    motorB.stop(stop_action="brake")
    motorC.stop(stop_action="brake")
    steering_motor.stop(stop_action="brake")

def turn():
    steering_motor.run_to_rel_pos(position_sp=90, speed_sp=500)


while True:
    ir_value = getIRValue()

    if (ir_value<=10):
        stop()
        break
    elif (ir_value < 50):
        turn()
    else:
        moveForward()
    



