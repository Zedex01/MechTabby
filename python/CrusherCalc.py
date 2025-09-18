""" Crusher Calculator """

import math
import numpy as np
import matplotlib.pyplot as plt


stack_size = 64
recipe_duration = 250
rpm = range(16, 256)
rpm = 16
rpm_range = range(16, 256)


#Compares 2 values and returns the smaller one
def getMin(x, y):
    if x >= y:
        return y
    else:
        return x

#Compares 2 values and returns the larger one
def getMax(x, y):
    if x < y:
        return y
    else:
        return x
        

def crushingTime(rpm, recipe_duration, stack_size):
    processing_time = ((recipe_duration - 20)/(getMax(0.25, getMin(((rpm * 4/50)/(math.log2(stack_size))),20)))) + 1
    return processing_time
        
def blocksPerSecond(rpm, recipe_duration, stack_size):
    #Procesing time in ticks / stack size      
    processing_time_ticks_stack = ((recipe_duration - 20)/(getMax(0.25, getMin(((rpm * 4/50)/(math.log2(stack_size))),20)))) + 1
    
    #processing_time_stack_seconds
    processing_time_sec_stack = processing_time_ticks_stack*20
    processing_time_sec_block = processing_time_sec_stack/stack_size
    return processing_time_sec_block
    
for rpm in range(16, 257):
    print(f"@ {rpm}, you crush {blocksPerSecond(rpm, recipe_duration, stack_size):.2f} blocks/sec and generate {2*8*rpm} combined su")
        
        
        
"""        
rpms = np.linspace(16, 256)
times = [crushingTime(rpm, recipe_duration, stack_size) for rpm in rpms]

times_sec = np.array(times) / 20.0

#plot
plt.plot(rpms, times_sec, label="Processing time (s)")
plt.xlabel("RPM")
plt.ylabel("Processing time (seconds per 64 cobble)")
plt.title("Create: Crushing Wheel Speed vs Processing Time")
plt.grid(True)
plt.legend()
plt.show()

print(crushingTime(256, recipe_duration, stack_size)/20)
"""