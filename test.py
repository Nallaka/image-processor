import KernelConvolve as convolve
import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
identity = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
output = convolve.convolve(x, "int", identity, False)

print(output)
