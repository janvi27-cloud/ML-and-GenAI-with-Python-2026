# Python Assignment: Functions

# 1. Function to print first 10 natural numbers
def print_first_10_natural_numbers():
    print("First 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print("\n")


# 2. Function to calculate sum of first N natural numbers
def sum_of_n_natural_numbers(n):
    return n * (n + 1) // 2


# 3. Function to reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev


# 4. Function to count digits in a number
def count_digits(num):
    if num == 0:
        return 1

    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


# 5. Function to check palindrome number
def is_palindrome(num):
    return num == reverse_number(num)


# 6. Function to generate Fibonacci series
def fibonacci_series(n):
    a, b = 0, 1
    series = []

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


# 7. Calculator Using Functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


def calculator():
    print("\n===== Calculator Using Functions =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result =", add(num1, num2))
        elif choice == '2':
            print("Result =", subtract(num1, num2))
        elif choice == '3':
            print("Result =", multiply(num1, num2))
        elif choice == '4':
            print("Result =", divide(num1, num2))
    else:
        print("Invalid Choice!")


# Main Program
if __name__ == "__main__":
    print_first_10_natural_numbers()

    n = int(input("Enter N to calculate sum of first N natural numbers: "))
    print("Sum =", sum_of_n_natural_numbers(n))

    num = int(input("\nEnter a number to reverse: "))
    print("Reversed Number =", reverse_number(num))

    num = int(input("\nEnter a number to count digits: "))
    print("Number of Digits =", count_digits(num))

    num = int(input("\nEnter a number to check palindrome: "))
    if is_palindrome(num):
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")

    terms = int(input("\nEnter number of Fibonacci terms: "))
    print("Fibonacci Series:", fibonacci_series(terms))

    calculator()

# Student Class
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Marks:", self.marks)


# Store details in file
name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))

student = Student(name, marks)

file = open("student.txt", "w")
file.write(f"Name: {student.name}\n")
file.write(f"Marks: {student.marks}\n")
file.close()

print("\nData stored successfully.")

# Read from file
print("\nReading File Contents:")
file = open("student.txt", "r")
print(file.read())
file.close()

# Display using class
student.display()

# Exception Handling
try:
    a = int(input("\nEnter first number: "))
    b = int(input("Enter second number: "))

    print("Division Result =", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")
