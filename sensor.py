#!/usr/bin/env python3

import ev3dev.ev3 as ev3 
from time import sleep

ir = ev3.InfraredSensor('in1') 
ir.mode = 'IR-PROX' 

for i in range(100):
    print(ir.value()) 