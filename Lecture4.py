# Access Array Element

import numpy as np

# 1-D array
print("1-D array:")
arr = np.array([1, 2, 3, 4])
print("Element at index 0:")
print(arr[0])
print("Element at index 1:")
print(arr[1])
print("Adding element at index 2 and index 3:")
print(arr[2] + arr[3])

# 2-D array
print("\n2-D array:")
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Element at index 1, row 0:")
print(arr1[0, 1])
print("Element at index 1, row 1:")
print(arr1[1, 1])
print("Element at index 4, row 0:")
print(arr1[0, 4])
print("Element at index 4, row 1:")
print(arr1[1, 4])
print("Adding element at index 2, row 0 and index 3, row 1:")
print(arr1[0, 2] + arr1[1, 3])

# 3-D array
print("\n3-D array:")
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Element at index 1, row 0, column 0:")
print(arr2[0, 0, 1])
print("Element at index 1, row 1, column 1:")
print(arr2[1, 1, 1])
print("Element at index 2, row 0, column 0:")
print(arr2[0, 0, 2])
print("Element at index 2, row 1, column :1")
print(arr2[1, 1, 2])
print("Adding element at index 2, row 0, column 0  and index 2, row 1, column 1:")
print(arr2[0, 0, 2] + arr2[1, 1, 2])
