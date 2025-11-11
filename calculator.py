a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Select an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

def division(a,b):
    return a/b

operation = input("Choose what operation you want to do\n")
print(division(a,b))