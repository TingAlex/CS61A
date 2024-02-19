# take a look at the plot of saw_wave and triangle_wave

import numpy as np
import matplotlib.pyplot as plt


# Define the saw_wave calculation as described
def saw_wave(t, period):
    return t / period - np.floor(t / period + 0.5)


# Define the triangle_wave calculation as described in the provided code
def triangle_wave(t, period):
    saw = saw_wave(t, period)
    tri = 2 * np.abs(2 * saw) - 1
    return tri


# Choose a period
period = 100  # for example purposes

# Generate a range of t values
t_values = np.linspace(0, 3 * period, 1000)  # three periods for illustration

# Calculate saw_wave values for these t values
saw_wave_values = saw_wave(t_values, period)
# Calculate triangle_wave values for the t values
triangle_wave_values = triangle_wave(t_values, period)

# Plot the saw_wave and triangle_wave results together
plt.plot(t_values, saw_wave_values, label='Saw Wave', color='blue')
plt.plot(t_values, triangle_wave_values, label='Triangle Wave', color='red')

plt.title('Saw Wave and Triangle Wave over Three Periods')
plt.xlabel('t (sample index)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
