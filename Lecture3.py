import numpy as np

# shaping of an array

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Shape of an array:")
print(arr.shape)

# Reshaping of an array
# 1-D to 2-D

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr1.reshape(4, 3)
print("\nConverting 1-D to 2-D:")
print(newarr)
print(newarr.shape)

# converting 1-D to 3-D
newarr1 = arr1.reshape(2, 3, 2)
print("\nConverting 1-D to 3-D:")
print(newarr1)
print(newarr1.shape)

# flattening of an array i.e. converting 2-D or 3-D to 1-D
newarr2 = arr.reshape(-1)
print("\nFlattening of an array:")
print(newarr2)
print(newarr2.shape)
