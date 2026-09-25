class Student:

    def __init__(self, name, department, cgpa):
        self.name = name
        self.department = department
        self.cgpa = cgpa

    def display(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("CGPA:", self.cgpa)

    def eligible(self):
        if self.cgpa >= 7.0:
            print(self.name, "is eligible")
        else:
            print(self.name, "is not eligible")


student1 = Student("Priya", "CSE", 8.5)

student1.display()
student1.eligible()