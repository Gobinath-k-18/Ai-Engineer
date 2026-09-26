import numpy as np

arr = np.arange(1, 13).reshape(3, 4)

print(arr)
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("First row:", arr[0])
print("Last column:", arr[:, -1])
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Mean:", np.mean(arr))