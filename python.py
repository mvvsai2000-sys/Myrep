Here’s a set of Python practice programs ranging from beginner to intermediate level, with complete runnable code and explanations.

1. Check if a Number is Prime
# Program to check if a number is prime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    n = int(input("Enter a number: "))
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
except ValueError:
    print("Invalid input! Please enter an integer.")

2. Reverse a String
# Program to reverse a string

text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

3. Fibonacci Sequence (n terms)
# Program to print Fibonacci sequence up to n terms

def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

try:
    terms = int(input("Enter number of terms: "))
    if terms <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci sequence:", fibonacci(terms))
except ValueError:
    print("Invalid input! Please enter an integer.")

4. Find Factorial (Recursive)
# Program to find factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {num} is {factorial(num)}")
except ValueError:
    print("Invalid input! Please enter an integer.")

5. Palindrome Checker
# Program to check if a string is a palindrome

text = input("Enter a string: ").lower()
if text == text[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")


✅ These programs cover loops, conditionals, functions, recursion, and string manipulation — perfect for practice.

If you want, I can prepare a full 30-day Python practice plan with increasing difficulty and real-world mini-projects.
Do you want me to create that next?
