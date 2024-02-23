#!/usr/bin/env python3 
import ev3dev.ev3 as ev3 

m = ev3.LargeMotor('outB')

m.run_timed(speed_sp=300, time_sp=1000)