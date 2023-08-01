# 21/X/20086/EVE
# GERIGA SUNDAY DRAGO

# DAY D
# Example
class Student:
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course

    def display_details(self):
        print("Name: ", self.name)
        print("Age: ", self.year)
        print("course: ", self.course)


std1 = Student("Geri", 3, "software Engineering")

std1.display_details()

print("====================================================")


# Circumference and area
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return 3.14 * self._radius * self._radius

    def calculate_circumference(self):
        return 3.14 * 2 * self._radius


shape1 = Circle(4)
print(shape1.calculate_area())
print(shape1.calculate_circumference())

print("====================================================")


# Exercise : Calculate and display employee bonuses(0.5) of salary (Employee1: 150000, employee: 230000)
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def calculate_bonuses(self, bonus_percentage):
        bonus_amount = self._salary * bonus_percentage
        return bonus_amount


# Create objects for employee
employee_one = Employee("Employee One :", 150000)
employee_two = Employee("Employee Two :", 230000)

# Create the bonus_percentages
bonus_percentage = 0.5
bonus_one = employee_one.calculate_bonuses(bonus_percentage)
bonus_two = employee_two.calculate_bonuses(bonus_percentage)

print(f"{employee_one.get_name()}: Bonus = {bonus_one}")
print("====================================================")
print(f"{employee_two.get_name()}: Bonus = {bonus_two}")
print("====================================================")


# Encapsulation
# Convert  temperature(37) from Celsius to Fahrenheit using encapsulation
# use
class Temperature:

    def __init__(self, celsius):
        self.__celsius = celsius

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, celsius):
        self.__celsius = celsius

    def to_fahrenheit(self):
        fahrenheit = (self.__celsius * 9 / 5) + 32
        return fahrenheit


converter = Temperature(37)
celsius_temp = converter.get_celsius()
fahrenheit_temp = converter.to_fahrenheit()

print(f"{celsius_temp} degrees Celsius is equal to {fahrenheit_temp} degrees fahrenheit ")
print("====================================================")


# Assignment 2: Show encapsulation with employee information to give pay incrementation
# (Salary with employee information to new salary ) e.g. from 850,000 to 1,000,000

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        # self.__age = age
        self.__salary = salary

    def get_name(self):
        return self.__name

    # def get_age(self):
    #     return self.__age

    def get_salary(self):
        return self.__salary

    def give_raise(self, increased_amount):
        increment_amount = self.__salary * (percentage / 100)
        self.__salary += increment_amount


emp = Employee("Geri", 850000)

# Display employee information before increment
print("Before increment")
print("Employee Name: ", emp.get_name())
# print("Employee Age: ", emp.get_age())
print("Employee salary: ", emp.get_salary())
print("====================================================")

# Increment salary
percentage = 17.65
emp.give_raise(percentage)

# Display update employee information
print("After increment")
print("Employee Name: ", emp.get_name() )
# print("Employee Age: ", emp.get_age())
print("Employee salary: ", emp.get_salary())
print("====================================================")
