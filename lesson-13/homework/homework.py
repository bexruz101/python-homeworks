import numpy as np

# Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)
print("Vector (10 to 49):\n", vector)

# Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("\n3x3 Matrix (0 to 8):\n", matrix_3x3)

# Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("\n3x3 Identity Matrix:\n", identity_matrix)

# Create a 3x3x3 array with random values
random_array = np.random.random((3, 3, 3))
print("\n3x3x3 Array with Random Values:\n", random_array)

# Create a 10x10 array with random values and find the minimum and maximum values
array_10x10 = np.random.random((10, 10))
min_value = np.min(array_10x10)
max_value = np.max(array_10x10)
print("\n10x10 Array with Random Values:")
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)

# Create a random vector of size 30 and find the mean value
random_vector = np.random.random(30)
mean_value = np.mean(random_vector)
print("\nRandom Vector (mean):", mean_value)

# Normalize a 5x5 random matrix
random_matrix_5x5 = np.random.random((5, 5))
normalized_matrix = (random_matrix_5x5 - np.mean(random_matrix_5x5)) / np.std(
    random_matrix_5x5
)
print("\nNormalized 5x5 Random Matrix:\n", normalized_matrix)

# Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
product_matrix = np.matmul(matrix_5x3, matrix_3x2)
print("\nMatrix Product (5x3) x (3x2):\n", product_matrix)

# Create two 3x3 matrices and compute their dot product
matrix1_3x3 = np.random.random((3, 3))
matrix2_3x3 = np.random.random((3, 3))
dot_product = np.dot(matrix1_3x3, matrix2_3x3)
print("\nDot Product of two 3x3 Matrices:\n", dot_product)

# Given a 4x4 matrix, find its transpose
matrix_4x4 = np.random.random((4, 4))
transpose_matrix = np.transpose(matrix_4x4)
print("\nTranspose of a 4x4 Matrix:\n", transpose_matrix)

# Create a 3x3 matrix and calculate its determinant
matrix_3x3_det = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3_det)
print("\nDeterminant of a 3x3 Matrix:\n", determinant)

# Create two matrices (A) (3x4) and (B) (4x3), and compute the matrix product (A * B)
matrix_A = np.random.random((3, 4))
matrix_B = np.random.random((4, 3))
matrix_product = np.matmul(matrix_A, matrix_B)
print("\nMatrix Product (A * B):\n", matrix_product)

# Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.
matrix_3x3 = np.random.random((3, 3))
vector_3 = np.random.random(3)
matrix_vector_product = np.matmul(matrix_3x3, vector_3)
print("\nMatrix-Vector Product:\n", matrix_vector_product)

# Solve the linear system (Ax = b) where (A) is a 3x3 matrix, and (b) is a 3x1 column vector.
A = np.random.random((3, 3))
b = np.random.random((3, 1))
x = np.linalg.solve(A, b)
print("\nSolution to Ax = b:\n", x)

# Given a 5x5 matrix, find the row-wise and column-wise sums.
matrix_5x5_sum = np.random.random((5, 5))
row_sums = np.sum(matrix_5x5_sum, axis=1)
column_sums = np.sum(matrix_5x5_sum, axis=0)
print("\nRow-wise Sums:\n", row_sums)
print("Column-wise Sums:\n", column_sums)
