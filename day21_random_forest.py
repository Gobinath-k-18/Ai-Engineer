
import pandas as pd

data = {
    "StudyHours": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 88, 92, 95],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print(df)
print("\nDataset shape:", df.shape)
