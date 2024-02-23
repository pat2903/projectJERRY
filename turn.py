import ev3dev.ev3 as ev3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from time import sleep

# Initialize the motors.
motorB = LargeMotor(OUTPUT_B)
motorC = LargeMotor(OUTPUT_C)

# To run both motors at the same speed.
motorB.run_forever(speed_sp=SpeedPercent(50))
motorC.run_forever(speed_sp=SpeedPercent(50))

sleep(4)

# Stop both motors.
motorB.stop(stop_action="coast")
motorC.stop(stop_action="coast")

# Alternatively, using MoveTank for synchronized movement.
# tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

# Move both motors forward for 2 seconds at 50% speed and then stop.
# tank_drive.on_for_seconds(SpeedPercent(50), SpeedPercent(50), 2)