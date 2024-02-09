import numpy as np
import matplotlib.pyplot as plt

# Read values from the text file
with open("11.9.1-11.txt", "r") as file:
    sequence_values = [int(line.strip()) for line in file][:6]  # Read only the first six values

# Generate values for n (indices)
n_values = np.arange(0, len(sequence_values))

# Plot the graph
plt.stem(n_values, sequence_values, use_line_collection=True)
plt.xlabel('n')
plt.ylabel('y(n)')
plt.show()

