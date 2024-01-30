import matplotlib.pyplot as plt
import numpy as np

# Read the sequence from the file
with open("sequence.txt", "r") as file:
    sequence = [int(line.strip()) for line in file]

# Convert the sequence to a NumPy array
sequence_array = np.array(sequence)

# Display the first five terms
print(f"First five terms: {sequence_array[:5]}")

# Plot the stem graph
plt.stem(range(len(sequence_array)), sequence_array, basefmt="k-", use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot of the Sequence')
plt.show()

