import pandas as pd

# --------------------------------------------------
# 1. Create messy dataset
# --------------------------------------------------

data = {
    "Name": ["Arun", "Bala", "Kumar", "Arun", "Divya"],
    "Age": ["21", "22", None, "21", "twenty"],
    "Marks": [85, 72, 91, 85, None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


# --------------------------------------------------
# 2. Inspect data
# --------------------------------------------------

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated())


# --------------------------------------------------
# 3. Remove duplicate rows
# --------------------------------------------------

df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)


# --------------------------------------------------
# 4. Fill missing Age
# --------------------------------------------------

df["Age"] = df["Age"].fillna("20")

print("\nAfter Filling Missing Age:")
print(df)


# --------------------------------------------------
# 5. Fix wrong Age value
# --------------------------------------------------

df["Age"] = df["Age"].replace("twenty", "20")

# Convert Age from string to integer
df["Age"] = df["Age"].astype(int)

print("\nAfter Cleaning Age:")
print(df)

print("\nData Types:")
print(df.dtypes)


# --------------------------------------------------
# 6. Fill missing Marks using mean
# --------------------------------------------------

mean_marks = df["Marks"].mean()

print("\nMean Marks:", mean_marks)

df["Marks"] = df["Marks"].fillna(mean_marks)

print("\nAfter Cleaning Marks:")
print(df)


# --------------------------------------------------
# 7. Final inspection
# --------------------------------------------------

print("\nFinal Data:")
print(df)

print("\nFinal Data Types:")
print(df.dtypes)

print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nFinal Duplicate Rows:")
print(df.duplicated().sum())