#inniate empty list and dict
students_list = []
students_dict = {}

# add student information
name = input("enter your name")
age = input("enter your age")
grade = input("enter your grade")
 #add student information

students_list.append(name)
students_dict[name] = {'age':age , "grade":grade}
print("Your information has been sucessfully saved")
print("students details")
#to display students details
print(name)
print(age)
print(grade)

#To search for the information
name = input("Enter name to search:")
if name in students_dict:
    info= students_dict[name]
    print("User has been found")
    print(name)
    print(age)
    print(grade)
else :
    print("Student not found")

