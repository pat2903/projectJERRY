import ev3dev.ev3 as ev3
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent
from time import sleep

# Initialize the motors.
motorB = LargeMotor(OUTPUT_B)
motorC = LargeMotor(OUTPUT_C)
steering_motor = MediumMotor(OUTPUT_A)

# To run both motors at the same speed.
motorB.run_forever(speed_sp=SpeedPercent(50))
motorC.run_forever(speed_sp=SpeedPercent(50))

# Don't know which way it's gonna turn w/ a positive angle. Let's find out :)
steering_motor.run_to_rel_pos(position_sp=45, speed_sp=SpeedPercent(50))

sleep(4)

# Stop both motors.
motorB.stop(stop_action="coast")
motorC.stop(stop_action="coast")