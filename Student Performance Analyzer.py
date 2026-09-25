name = input("Enter student name: ")

try:
    maths = int(input("Enter Maths mark: "))
    science = int(input("Enter Science mark: "))
    english = int(input("Enter English mark: "))
    attendance = float(input("Enter attendance percentage: "))

except ValueError:
    print("Please enter valid numbers.")
    exit()

if maths < 0 or maths > 100:
    print("Maths mark must be between 0 and 100.")
    exit()

if science < 0 or science > 100:
    print("Science mark must be between 0 and 100.")
    exit()

if english < 0 or english > 100:
    print("English mark must be between 0 and 100.")
    exit()

if attendance < 0 or attendance > 100:
    print("Attendance must be between 0 and 100.")
    exit()

total = maths + science + english
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

if average >= 50 and attendance >= 75:
    result = "Pass"
else:
    result = "Fail"

print("\n--- Student Performance Report ---")
print("Name:", name)
print("Maths:", maths)
print("Science:", science)
print("English:", english)
print("Total:", total)
print("Average:", round(average, 2))
print("Attendance:", attendance, "%")
print("Grade:", grade)
print("Result:", result)