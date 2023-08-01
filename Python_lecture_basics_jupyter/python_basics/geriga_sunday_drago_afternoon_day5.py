# Day 5
# Error handling and file handling

# 1. Error handling
# Exception and file handling
# 1. Exception/ Error handling
# types of exceptions/errors
# SyntaxError -> This exception arise when the interpreter encounters a syntax error in the code s
# such as misspelled keyword or missing colons

code = """
print("Geri Sunday")
"""
try:
    exec(code)
except SyntaxError as t:
    print("Syntax Error", str(t))

# TypeError -> This occurs when an operation or function is applied to an object of wrong type e.g.
# adding a string and an integer

try:
    x = 5
    y = "Drago"
    z = x + y
    print(z)
except TypeError:
    print("TypeError")

# NameError -> This occurs when a variable or function is not found in the current scope
try:
    x = 5
    y = "Geriga"
    z = x + y
    print(z)
except TypeError:
    print("NameError")

# IndexError -> This occurs when an index is out of range of a tuple, list:

x = [20, 30, 40]
try:
    print(x[4])
except IndexError:
    print("Index Error")

# KeyError ->This occurs when the key to be retrieved is not available in the dictionary

vehicle = {"Brand": "Toyota", "Model": "Camry"}
try:
    print(vehicle["color"])
except KeyError:
    print("Key error")

# ValueError -> This occurs when a function or method is called with an invalid argument or input
# e.g. tying to convert a string to integer when the string does not represent a valid integer
try:
    age = input("Enter your age")
    age = int(age)
    if age < 0:
        raise valueError("Age can not be negative")
    print("Your age is ", age)
except ValueError as e:
    print("Invalid age :", str(e))


# AttributeError -> occurs when trying to access a non-existent attribute of a class instance
class Swift:
    def __init__(self, value):
        self.value = value


my_obj = Swift(10)

try:
    print(my_obj.name)
except AttributeError:
    print("Attribute not found")
# IOError -> Occurs when reading or writing a file fails due to an input/output error
try:
    file = open("school.tx", "r")
except IOError:
    print("I/O error")

# ZeroDivisionError -> This occurs when dividing a number by zero
try:
    numerator = int(input("Enter the numerator"))
    denominator = int(input("Enter the denominator"))
    result = numerator / denominator
    print("Result: ", result)
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid input, please enter integers")

# ImportError ->occurs when importing a module that does not exist
try:
    import pandas as pd

    print("Pandas version", pd.__version)
except ImportError:
    print("Error: Pandas module not found. Please install pandas")

# File handling
# This allows one to perform operations on files such as opening, reading and writing in to a file
# Tasks performed includes;
# 1. Opening a file -> To perform this one can use built-in 'open()' function which takes 2 parameters
# ie the file path/name and the mode 'r' or 'w' for reading or writing

file = open("school.txt", "r")

# 2. Reading the file content -> To read the content of the file, one can use either read(), readline()
# or readlines()
content = file.read()
print(content)

# 3. Writing in to a file -> Here one needs to open the file in write mode("w") or append mode("a")
file = open("school.txt", "w")
file.write("Drago Sunday must attend lectures everytime without missing")
file.close()

# 3. Closing a file -> It is paramount to always close the file you have been working on using
# close() function to free up resources.
# alternatively, one can use with statement which automatically closes the file
with open("school.txt", "r") as file:
    content = file.read()
    print(content)

# However it is prudent to also handle errors with file operation
try:
    file = open("school.txt", "r")
    content =file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
