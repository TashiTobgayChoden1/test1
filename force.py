print("newtons second law of motion")
print("-----------------------")
# Determine the missing value
print("Select the missing values")
print("1. Mass(m)")
print("2. Acceleration(a)")
print("3. force(f)")
missing_value_choice= input("enter the option number for the missing value:")

# Prompt the user to enter the other two values
if missing_value_choice=="1":
    a=float(input("Enter acceleration(a):"))
    F=float(input("Enter force(f):"))
    m=F/a
    print(f"Mass(m)={m}")

elif missing_value_choice=="2":
    m=float(input("enter the mass(m):"))
    F=float(input("enter the force(f):"))
    a=F/m
    print(f"Acceleration (a)={a}")