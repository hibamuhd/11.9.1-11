import matplotlib.pyplot as plt
import numpy as np


with open("11.9.1-11.txt", "r") as file:
    sequence = [int(line.strip()) for line in file]


sequence_array = np.array(sequence)


def sequence_a(n):
    return -1 if n == 0 else 3 * 3**n


n_values = np.arange(0, 11, 1)


a_values = [sequence_a(n) for n in n_values]


plt.stem(range(len(sequence_array)), sequence_array, basefmt="k-", linefmt="b-", markerfmt="bo", label='Sequence from normal method', use_line_collection=True)
plt.stem(n_values, a_values, basefmt="k-", linefmt="r-", markerfmt="ro", label='Sequence from z transfrom inverse', use_line_collection=True)

plt.xlabel('n')
plt.ylabel('Value')
plt.title('Comparison of Sequences')
plt.legend()
plt.grid(True)
plt.show()


