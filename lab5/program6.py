import numpy as np
# Create a 2D array
arr = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])
# Slice every second row and column
sliced_arr = arr[::2, ::2]
#sliced_arr = arr[1:, 2:]
print("Sliced Array with Steps:\n", sliced_arr)
