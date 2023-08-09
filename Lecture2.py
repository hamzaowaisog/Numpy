import numpy as np

# 1. creating 0-D array
arr = np.array(42)
print(arr)
print(arr.ndim)
# 2. creating 1-D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(arr1.ndim)

# 3. creating 2-D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print(arr2.ndim)

# 4. creating 3-D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3)
print(arr3.ndim)
