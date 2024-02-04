import numpy as np
import matplotlib.pyplot as plt

# Function to calculate a_n
def sequence(n):
    return -1 + 3 * (3 ** n) if n >= 0 else 0

# Generate values for n in the range from 5 to -5
n_values = np.arange(5, -6, -1)

# Calculate corresponding values for a_n
a_n_values = [sequence(n) for n in n_values]

# Plot the sequence
plt.stem(n_values, a_n_values, basefmt='k-', linefmt='b-', markerfmt='bo', use_line_collection=True)
plt.title(r'$a_n = -u_n + 3(3^n u_n)$')
plt.xlabel('$n$')
plt.ylabel('$a_n$')
plt.grid(True)
plt.show()

