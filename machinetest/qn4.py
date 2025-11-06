class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


calcu = Calculator()

a = float(input("Enter a:"))
b = float(input("Enter b:"))

print("Select operation: +, -, *, /")
operation = input("Enter operation: ")

if operation == '+':
    print(f"{a} + {b} = {calcu.add(a, b)}")
elif operation == '-':
    print(f"{a} - {b} = {calcu.subtract(a, b)}")
elif operation == '*':
    print(f"{a} * {b} = {calcu.multiply(a, b)}")
elif operation == '/':
    print(f"{a} / {b} = {calcu.divide(a, b)}")
else:
    print("Invalid operation")


