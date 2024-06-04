import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# Define the power functions
def power_func(x, exponent):
    return x**exponent


# Parameters for the functions
a = 0.5
b = 0.3

# Generate x values
x = np.linspace(0, 1, 500)

# Calculate y values
y1 = power_func(x, a)
y2 = power_func(x, b)

# Integrate to find the area under the curves
integral1, _ = quad(lambda x: power_func(x, a), 0, 1)
integral2, _ = quad(lambda x: power_func(x, b), 0, 1)

# Normalize the curves to have the same integral
y1_normalized = y1 / integral1
y2_normalized = y2 / integral2

# Plot the curves
plt.plot(x, y1_normalized, label="$x^{0.5}$")
plt.plot(x, y2_normalized, label="$x^{0.3}$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
