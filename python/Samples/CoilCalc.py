import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Circuit parameters
L = 300e-3     # Inductance in Henrys (e.g., 1 mH)
R = 0.001      # Resistance in Ohms
C = 390e-6     # Capacitance in Farads (e.g., 1 uF)

# Define the system of ODEs
def lrc_ode(t, x):
    x1, x2 = x
    dx1dt = x2
    dx2dt = -(R / L) * x2 - (1 / (L * C)) * x1
    return [dx1dt, dx2dt]

# Initial conditions: current and its derivative
i0 = 0.0     # Initial current (A)
di0_dt = 1.0  # Initial current derivative (A/s) — example

# Time span for the solution
t_span = (0, 0.05)  # seconds
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the ODE
sol = solve_ivp(lrc_ode, t_span, [i0, di0_dt], t_eval=t_eval)

# Plot the current i(t)
plt.plot(sol.t, sol.y[0])
plt.title("Current i(t) in Series LRC Circuit")
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.grid(True)
plt.show()
