class Person:
    def __init__(self, name, age, cid):
        self.name = name
        self.age = age
        self.cid = cid

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Teacher(Person):
    def __init__(self, name, age, cid, subject, salary, department, designation):
        super().__init__(name, age, cid)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")


class Student(Person):
    def __init__(self, name, age, cid, student_id, course, year, gpa):
        super().__init__(name, age, cid)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

    def write_exam(self):
        print(f"{self.name} is writing an exam.")

# Create a teacher instance
teacher = Teacher("John Doe", 35, "123456", "Mathematics", 50000, "Science", "Professor")
teacher.teach()
teacher.grade_students()

# Create a student instance
student = Student("Jane Smith", 20, "789012", "123456789", "Computer Science", 2, 3.8)
student.study()
student.attend_class()
student.write_exam()
    
   


