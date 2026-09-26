import numpy as np

arr = np.arange(1, 13)

print("Original:", arr)
print("Shape:", arr.shape)

matrix = arr.reshape(3, 4)

print("Matrix:")
print(matrix)

print("Mean:", np.mean(matrix))
print("Median:", np.median(matrix))
print("Std:", np.std(matrix))
print("Min:", np.min(matrix))
print("Max:", np.max(matrix))

print("After adding 10:")
print(matrix + 10)

print("Transpose:")
print(matrix.T)