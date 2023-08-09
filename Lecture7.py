# Searching and Sorting of Arrays

import numpy as np

# Searching
# 1-D array
print("Searching")
print("1-D array:")
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
x = np.where(arr % 2 == 0)
print(x)

# 2-D array
print("\n2-D array:")
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
x = np.where(arr1 == 4)
print(x)
x = np.where(arr1 % 2 == 0)
print(x)

# 3-D array
print("\n3-D array:")
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [4, 10, 11]]])
x = np.where(arr2 == 4)
print(x)
x = np.where(arr2 % 2 == 0)
print(x)


# Sorting
# 1-D array
print("Sorting")
print("1-D array:")

arr = np.array([1, 2, 3, 4, 5, 4, 4])
print(np.sort(arr))
print(np.sort(arr)[::-1])

arr_fruit = np.array(["mango", "apple", "banana", "cherry"])
print(np.sort(arr_fruit))

# 2-D array
print("\n2-D array:")
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np.sort(arr1))
arr1 = arr1.reshape(-1)
arr1 = np.sort(arr1)[::-1]
arr1 = arr1.reshape(2, 5)
print(arr1)

# 3-D array
print("\n3-D array:")
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [4, 10, 11]]])
print(np.sort(arr2))
arr2 = arr2.reshape(-1)
arr2 = np.sort(arr2)[::-1]
arr2 = arr2.reshape(2, 2, 3)
print(arr2)
