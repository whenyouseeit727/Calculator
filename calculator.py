
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Select an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Choose what operation you want to do\n")


def subtraction(a, b):
    return a - b
def addition(a, b):
    return a + b
def division(a, b):
    return a/b
def multiply(a, b):
    return a*b

if operation == "1":
    result = addition(a,b)
    print(result)
elif operation == "2":
    result=subtraction(a,b)
    print(result)
elif operation == "3":
    result=multiply(a,b)
    print(result)
elif operation == "4":
    result=division(a,b)
    print(result)















