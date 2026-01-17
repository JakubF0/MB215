# get two values from the user
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))

# perform calculations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# zero check
if b != 0:
    print("Division:", a / b)
    print("Integer Division:", a // b)
    print("Remainder:", a % b)
else:
    print("Division, Integer Division, Remainder: Cannot divide by zero")

print("Exponent:", a ** b)
