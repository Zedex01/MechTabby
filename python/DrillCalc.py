"""DrillCalc"""

"""
Stress Units are equal to RPM * 4
Breaking Speed (seconds )is equal to  (45 * hardness)/ RPM

Cobble Hardness is 2 

Max RPM is 256
Min RPM is 16

"""

import math
import numpy as np
import matplotlib.pyplot as plt


num_drills = 24



def blocksPerSecond(num_drills, hardness, rpm):
    seconds_per_block = 45 * hardness / rpm
    blocks_per_seconds = 1/seconds_per_block
    
    bps = num_drills * blocks_per_seconds
    return bps

def stress(num_drills, rpm):
    return num_drills * 4 * rpm
    
    
def calculate(num_drills, hardness, rpm):
    bps = blocksPerSecond(num_drills, hardness, rpm)
    su = stress(num_drills, rpm)
    print(f"For {num_drills} drills @ {rpm}rpm, you will break {bps:.2f}/sec and generate {su}su")
    
    
num_drills = 24
hardness = 2

for rpm in range(16,257):
    calculate(num_drills, hardness, rpm)
    
    
    
    
