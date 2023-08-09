# Iterating Arrays

import numpy as np

# 1-D array
print("1-D array:")
arr = np.array([1, 2, 3, 4])
for x in arr:
    print(x)

# 2-D array
# Iterating each dimension of 2-D array
print("\n2-D array:")
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Iterating each dimension of 2-D array:")
for x in arr1:
    print(x)

# Iterating each scalarq element of 2-D array
print("\nIterating each scalar element of 2-D array:")
for x in arr1:
    for y in x:
        print(y)
