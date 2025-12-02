# --------------------------------------------
# Topic 2: NumPy Basics - Generative AI B.Tech Core
# --------------------------------------------

import numpy as np

# 1D Array
oned_array = np.array([1, 2, 3])
print("1D Array:", oned_array)
print("Dimensions:", oned_array.ndim)

# Row Vector (2D)
row_vector = np.array([[1, 2, 3]])
print("\nRow Vector:\n", row_vector)
print("Dimensions:", row_vector.ndim)
print("Shape:", row_vector.shape)
print("Size:", row_vector.size)

# Column Vector
column_vector = row_vector.transpose()
print("\nColumn Vector:\n", column_vector)

# Rank One Vector
rank_one_vector = np.array([1, 2, 3])
print("\nRank One Vector:", rank_one_vector)

# 2D Array
twod_array = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", twod_array)

# Indexing
print("\nIndexing Example:")
print(twod_array[0][1])  # 2
print(twod_array[1][2])  # 6

# Slicing
print("\nSlicing Example:\n", twod_array[:, 0:2])

# Matrix using np.matrix
mat1 = np.matrix("1,2,3;4,5,6;7,8,9")
print("\nMatrix:\n", mat1)

# Random Array
random_array = np.random.random((3, 3))
print("\nRandom Array:\n", random_array)

# Random Integers
randint_array = np.random.randint(1, 10, (3, 3))
print("\nRandom Integer Array:\n", randint_array)

# Mathematical Operations
data = np.array([1, 2, 3, 4])
print("\nOriginal:", data)

power_data = np.power(data, 2)
print("Power 2:", power_data)

exp_data = np.exp(data)
print("Exponential:", exp_data)

log_data = np.log(data)
print("Natural Log:", log_data)

log2_data = np.log2(data)
print("Log base 2:", log2_data)

log10_data = np.log10(data)
print("Log base 10:", log10_data)

# Zeros and Ones
zeros_array = np.zeros((3, 3), dtype=int)
print("\nZeros Array:\n", zeros_array)

ones_array = np.ones((2, 3), dtype=int)
print("\nOnes Array:\n", ones_array)
