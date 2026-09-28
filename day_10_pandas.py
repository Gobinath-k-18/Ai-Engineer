import pandas as pd

df = pd.read_csv("students.csv")


print("\nStatistical Summary:")
print(df.describe())