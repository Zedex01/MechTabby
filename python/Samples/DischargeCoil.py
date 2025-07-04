import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

R = 0.01      # Resistance in Ohms
C = 390e-6     # Capacitance in Farads (e.g., 1 uF)

e=2.719

T = R*C
FT = 5*T
print(f"Time Constant: {T} s")
print(f"5T: {FT} s")

time = np.linspace(0,6*T,400)

# Initial conditions: current and its derivative
v0 = 450.0  #Initial Voltage

#Voltage over time for discharge
v = v0*(e**(-1*time/T))

#Current over TimeFor DIscharge
i0 = v0/R #Initial current

i = i0*(e**(-time/T))
 
#Plot the Voltage V(t)
plt.plot(time, v)
plt.title("Voltage V(t) in Discharging RC Circuit")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.show()   

#Plot the Current i(t)
plt.plot(time, i)
plt.title("Current A(t) in Discharging RC Circuit")
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.grid(True)
plt.show()     
      
    
