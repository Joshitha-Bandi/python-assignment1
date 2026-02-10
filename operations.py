# Take two numbers as input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform basic operations
addition = a + b
subtraction = a - b
multiplication = a * b

# Handle division safely
if b != 0:
    division = a / b
else:
    division = "Cannot divide by zero"

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)