import csv

# Get student details safely
name = input("Enter student name: ")

try:
    age = int(input("Enter student age: "))

except ValueError:
    print("Please enter a valid age.")
    exit()

# Write to TXT file
with open("students.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n")

# Read TXT file
print("\nStudent Details:")

with open("students.txt", "r") as file:
    content = file.read()
    print(content)

# Write to CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age"])
    writer.writerow([name, age])

print("Student data saved successfully!")