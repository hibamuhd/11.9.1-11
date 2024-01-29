import matplotlib.pyplot as plt

# Read sequence values from the txt file
with open('sequence_values.txt', 'r') as file:
    sequence_values = [int(line.strip()) for line in file]

# Generate n values from 1 to 8
n_values = list(range(1, len(sequence_values) + 1))

# Plotting the graph
plt.plot(n_values, sequence_values, marker='o')
plt.title('Sequence: xn = 3xn-1 + 2')
plt.xlabel('n')
plt.ylabel('Sequence Value')
plt.grid(True)
plt.show()

