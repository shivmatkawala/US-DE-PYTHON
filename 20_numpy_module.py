 # Numpy:
    # Numpy is python library for numerical computing.
    # It provides efficient multidiamensional array and
    # mathematical operations.

import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])
# print(numbers)
# print(type(numbers))
# print(numbers * 2)
# print(numbers.mean())
# print(numbers.max())
# print(numbers.min())

nums = np.arange(1, 10, 2)
# print(nums)
# print(type(nums))

ones_arr1 = np.ones((3, 2))
# print(ones_arr1)

zeros_arr1 = np.zeros((3, 3))
# print(zeros_arr1)

my_arr1 = np.linspace(1, 2, 5)
# print(my_arr1)

arr2 = np.eye(5)
# print(arr2)

#--------------------------------------------
# Diamensions and shape:
arr3 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# print(arr3)
# print(arr3.ndim)
# print(arr3.shape)
# print(arr3.dtype)
# print(arr3.size)

#---------------------------------
arr4 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
# print(arr4[0])
# print(arr4[-1])
# print(arr4[1: 4])
# print(arr4[::2])
# print(arr4[::-1])
# print(arr4)

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(matrix[0, 0])
print(matrix[1, 2])
# print(matrix[2, 2])

tensor = np.array([
    [
        [1, 2, 3],
        [5, 6, 7]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

# print(tensor[0, 0, 0])
# print(tensor[1, 0, 1])

# Aggregations:

arr5 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# print(np.sum(arr5))
# print(np.sum(arr5, axis=0))
# print(np.sum(arr5, axis=1))


# Filtering And Reshaping:
arr6 = np.array([10, 25, 30, 45, 50, 60])
# print(arr6>30)
# print(arr6[arr6 > 30])

# arr6_2d = arr6.reshape((2, 3))
print(arr6_2d)

#-------------------