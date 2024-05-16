# Assigment
# get user input for age and student status
age=int(input("Enter your Age:"))
is_student_str=input("Are you student?(yes/no)")
# convert the input string into boolean value
is_student=is_student_str=="yes"
# define the age limit for discount
age_limit=12
#check discount eligibility using logical conditions
if age<=age_limit or is_student:
    print("you are eligible for discount on the movie ticket")
else:
    print("sorry, you are not eligible for the discount on the movie ticket")