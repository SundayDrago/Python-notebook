# Day 6
# Advanced topics in Python

"""
-Regular expressions
-Generators and iterators
-Decorators
-Context managers
-Multithreading and multiprocessing
"""

# Match first word
#reg re.match(), re.search(), re.findall()
#Example 1: Demonstrating regex / Match first word, match group word, match all numbers
import re
text ="hello, my name is Geriga. I am a programmer with 2years experience"

#Match first word
match = re.search(r"\b\w+\b", text)

if match:
    print("Match: ", match.group())
print("=======================================================")
matches = re.findall(r"\d+", text)
print("Matches :", matches)

# # # Example 2: validate email format or email address
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    return match is not None

# Test email addresses
emails = ['sundaydrago120@gmail.com', 'sundaydrago@gmail.com', 'invalid_email', 'test@123']

for email in emails:
    if validate_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is an invalid email address.")



# Generator and iterators
# 'yield' generator 
# Iterator '__iter__' "__next__" iterator

# #Example 2 : Create a function that returns factorial of the number of
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
    #Print the factorial of number from 1 -10
for i in range(1,10):
        print(i, "! = ", factorial(i))
print("=====================================================")

# #Example 3 : Create a function that returns factorial of the number of
def factorial(n):
    if n == 0:
        yield 1
    else:
        yield n * next(factorial(n - 1))

# Print the factorial of numbers from 1 to 9
for i in range(1, 10):
    print(i, "! =", next(factorial(i)))
print("================================================================")
#Example 3: Iterator using a class

class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration()

# Using the iterator
my_iterator = MyIterator(5)
for item in my_iterator:
    print(item)

print("=====================================================")
# Example 4: Using generator
def my_iterator(limit):
    current = 0
    while current < limit:
        yield current
        current += 1

# Using the iterator
for item in my_iterator(5):
    print(item)

print("=====================================================")

# Example 4
# Generate functions that yield the square of numbers from 1-10
def my_square():
    for i in range(1,11):
        yield i**2

# Create the iterator that yields the square of numbers from 1-10
my_iterator = my_square()

# Print the first 5 squares of numbers
for i in range(5):
    print(next(my_iterator))

print("=====================================================")

# Decorators @my_decorators
# 

def my_decorator_function(original_function):
    def wrapper_function():
        print("Before decorator function is called")
        original_function()
        print("After decorator function is called")
        return wrapper_function()
    
@my_decorator_function
def decorated_function():
    print("Inside decorated function")

decorated_function()
print("=====================================================")
