import numpy as np

new_max_float = 0.6    
new_min_float = 0

values = np.arange(new_min_float, new_max_float + 0.01, 0.01)

FN = np.percentile(values, 7)
MW = np.percentile(values, 15)
FT = np.percentile(values, 38)
WW = np.percentile(values, 45)

print("Targets: ")
print("FN: ", FN)
print("MW: ", MW)
print("FT: ", FT)
print("WW: ", WW)
print("BS: 1")


def remap(value, old_min, old_max, new_min, new_max):
    return new_min + (value - old_min) * (new_max - new_min) / (old_max - old_min)

value = 0.11999999
old_min = 0
old_max = 0.6
new_min = 0
new_max = 1

print("OG: ", value)
new_value = remap(value, old_min, old_max, new_min, new_max)

print("Adjusted: ", new_value)


"""
Lets hypothetically craft a FN M4A1-S Nitro
Range is: 0.06 -> 0.80
0.06 - 0.07 FN

0.80-0.06 = 0.74
Range of 74
0.06/0.74 = 0.081 (Adj Value)
then use tradeup formula and make sure it is less that adj value



"""