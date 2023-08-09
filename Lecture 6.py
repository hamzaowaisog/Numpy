# ARRAYS SLICING

import numpy as np

# 1-D array
print("1-D array:")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr[1:6])
print(arr[0::2])

# 2-D array
print("\n2-D array:")
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr1[1, 1:4])
print(arr1[0:2, 2:4])

# 3-D array
print("\n3-D array:")
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr2[0, 1, 1:3])
print(arr2[1, 0:2, 1:3])
print(arr2[0:2, 0:2, 0:3])
print(arr2[0:2, 0:2, 0:3:2])