# Prompt the user to enter the number and the limit
num = int(input("Enter the number for which you want the multiplication table: "))
limit = int(input("Enter the limit up to which you want the multiplication table: "))

# Print the multiplication table
print(f"\nMultiplication Table for {num} up to {limit}:")
for i in range(1, limit + 1):
    result = num * i
    print(f"{num} x {i} = {result}")