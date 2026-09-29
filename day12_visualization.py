""" import matplotlib.pyplot as plt

students = ["Arun", "Bala", "Kumar", "Divya"]
marks = [85, 72, 91, 83]

plt.bar(students, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show() """

""" import matplotlib.pyplot as plt

marks = [45, 52, 55, 58, 61, 63, 67, 70, 72, 75, 78, 82, 85, 90]

plt.hist(marks, bins=5)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Marks")

plt.show() """

""" import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 58, 65, 72, 85]

plt.scatter(study_hours, marks)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.show() """


""" import matplotlib.pyplot as plt

marks = [45, 52, 55, 58, 61, 63, 67, 70, 72, 75, 78, 82, 85, 90, 5]

plt.boxplot(marks)

plt.ylabel("Marks")
plt.title("Student Marks Box Plot")

plt.show() """

""" import seaborn as sns
import matplotlib.pyplot as plt

students = ["Arun", "Bala", "Kumar", "Divya"]
marks = [85, 72, 91, 83]

sns.barplot(x=students, y=marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show() """

""" import pandas as pd

data = {
    "StudyHours": [1, 2, 3, 4, 5, 6],
    "Marks": [45, 50, 58, 65, 72, 85]
}

df = pd.DataFrame(data)

print(df.corr()) """


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Student": ["Arun", "Bala", "Kumar", "Divya", "Ravi", "Priya", "Suresh", "Meena"],
    "StudyHours": [1, 2, 3, 4, 5, 6, 2, 4],
    "Marks": [45, 50, 58, 65, 72, 85, 52, 68]
}

df = pd.DataFrame(data)

print(df)
""" 
plt.bar(df["Student"], df["Marks"])

plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show() """

""" plt.hist(df["Marks"], bins=5)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Marks")

plt.show() """
""" plt.scatter(df["StudyHours"], df["Marks"])

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.show() """

""" plt.boxplot(df["Marks"])

plt.ylabel("Marks")
plt.title("Student Marks Box Plot")

plt.show() """
""" sns.barplot(x="Student", y="Marks", data=df)

plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks using Seaborn")

plt.show() """
correlation = df[["StudyHours", "Marks"]].corr()

print(correlation)
sns.heatmap(correlation, annot=True)

plt.title("Study Hours and Marks Correlation")

plt.show()