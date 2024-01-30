import matplotlib.pyplot as plt

# Read the sequence from the file
with open("sequence.txt", "r") as file:
    sequence = [int(line.strip()) for line in file]

# Display the first five terms
for n, value in enumerate(sequence):
    print(f'x{n} = {value}')

# Plot the stem graph
plt.stem(range(6), sequence, basefmt="k-", use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot of the Sequence')
plt.show()

