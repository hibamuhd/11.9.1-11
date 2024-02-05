import matplotlib.pyplot as plt
import numpy as np

# Define the function for a(n)
def sequence_a(n):
    return -1 if n == 0 else 3 * 3**n

# Generate values for n from 0 to 10
n_values = np.arange(0, 11, 1)

# Calculate the corresponding values for a(n)
a_values = [sequence_a(n) for n in n_values]

# Plot the sequence with smaller y-axis values
plt.stem(n_values, a_values, use_line_collection=True)
plt.xlabel('n')
plt.ylabel('a(n)')
plt.title('Sequence $a(n) = -u_n + 3(3^n u_n)$')

# Set y-axis limits to have smaller values
plt.ylim(min(a_values) - 1, max(a_values) + 1)

plt.grid(True)
plt.show()

