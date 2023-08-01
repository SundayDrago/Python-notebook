# Inheritance -> Allows creation of a class on already existing class which is also called subset

# class CircleShape(shape):
# Example One
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating ...")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking..")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing..")


# Create Animal objects
animal = Animal("Generic Animals")
dog = Dog("Cobra")
cat = Cat("Rambo")

# Invoke eat method
animal.eat()
cat.meow()
cat.eat()
dog.eat()
dog.bark()

print("=========================================================================================================")


# Example 2: Demonstrate concept of inheritance

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print("Brand: ", self.brand)
        print("Color: ", self.color)


class Car(Vehicle):
    def __init__(self, brand, color, num_wheels):
        super().__init__(brand, color)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print(f"Number of wheels : {self.num_wheels}")


# Creating an instance of vehicle class
vehicle = Vehicle("Generic Brand", "Generic Color")
vehicle.display_info()
print()

# Creating an instance of car class
car = Car("Toyota", "Red", 2)
car.display_info()
print("========================================================================================================")


# Exercise 1: Demonstrate using inheritance to calculate area and perimeter of a circle and rectangle respectively
# Create base class to be shape


class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


# Create Circle class that inherits from shape class

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)


# Creating an instance for the Circle class
circle = Circle(5)
print("Area of a Circle", circle.calculate_area())
print("Perimeter of a Circle", circle.calculate_perimeter())
print()

# Creating an instance for the Circle class
recta = Rectangle(5, 8)
print("Area of a Circle", recta.calculate_area())
print("Perimeter of a Circle", recta.calculate_perimeter())
print("=======================================================================================================")


#
# # # Example 3:
# # # Multiple inheritance
# # #
class TerrestrialAnimal:
    #Constructor
    def __init__(self, habitat):
        self.habitat = habitat
#method function
    def show_habitat(self):
        print(f"habitat: {self.habitat}")


class AquaticAnimal:
    def __init__(self, water_type):
        self.water_type = water_type

    def show_water_type(self):
        print(f"Water Type: {self.water_type}")

# Multiple inheritance 
class WildAnimal(TerrestrialAnimal, AquaticAnimal):
    def __init__(self, species, habitat, water_type):
        TerrestrialAnimal.__init__(self, habitat)
        AquaticAnimal.__init__(self, water_type)
        self.species = species

    def show_info(self):
        print(f"Species: {self.species}")
        self.show_habitat()
        self.show_water_type()


# Creating an instance of the WildAnimal
tiger = WildAnimal("Tiger", "Land", "None")
tiger.show_info()
print()

shark = WildAnimal("Shark", "None", "SaltWater")
shark.show_info()
print()

print("==========================================================================================================")


# # # Method overriding
class Animal:
    def eat(self):
        print("Animal is making a sound")


class Dog(Animal):
    def eat(self):  # Overriding the method
        print("Dog eats bones")


class Cat(Animal):
    def eat(self):
        print("Cat eats fish/rats")


# Create an object
animal = Animal()
dog = Dog()
cat = Cat()

dog.eat()
cat.eat()

print("==========================================================================================================")


# # # polymorphism ->  two methods
# 1. overriding
# 2. overloading
# Example 4
# Using the example of area of a circle to implement the concept of method overriding in polymorphism
#
class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_circumference(self):
        return 2 * 3.14 * self.radius

        # Create objects


rectangle = Rectangle(5, 7)
circle = Circle(8)

# Display the calculate area
print("Circle Area", circle.calculate_area())
print("Rectangle Area", rectangle.calculate_area())
print("==========================================================================================================")


# 2. Method overloading


class OperateMath:
    def add(self, a, b, c=None):
        if c is None:
            return b + a
        else:
            return a + b + c


# Create an object of OperateMath
math = OperateMath()

# Calling the add() function with two arguments
answerOne = math.add(2, 5)
print("Answer One: ", answerOne)

# Calling the add() function with two arguments
answerTwo = math.add(2, 5, 3)
print("Answer Two: ", answerTwo)

print("==========================================================================================================")
# Abstraction -> Demonstrate abstraction
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        pass

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def start(self):
        return f"{self.brand} {self.model} started."

    def stop(self):
        return f"{self.brand} {self.model} stopped."


class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def start(self):
        return f"{self.brand} {self.model} started."

    def stop(self):
        return f"{self.brand} {self.model} stopped."


# Creating an instance for Car class
car1 = Car("Toyota", "Camry")
print(car1.start())
print(car1.stop())

# Creating an instance for Car class
motorcycle = Car("Honda", "CBR500R")
print(motorcycle.start())
print(motorcycle.stop())

print("==========================================================================================================")
# Assignment
# Create a receipt a printing program with GUI interface

import tkinter as tk


def print_receipt():
    # Retrieve information from input fields
    item_name = item_entry.get()
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())

    # Calculate the total price
    total_price = quantity * price

    # Creating some of the receipt strings
    receipt = f"Item : {item_name}\n"
    receipt += f"Quantity : {quantity}kg\n"
    receipt += f"Price : Ugh.{price:.2f}\n"
    receipt += f"Total : Ugh.{total_price: .2f}"

    # Print receipt
    print(receipt)

    # for clearing input fields
    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)


# Creating windows
window = tk.Tk()
window.title("GERIGA'S RECEIPT PRINTING PROGRAM")

# Creating input labels and fields
item_label = tk.Label(window, text="Item: ")
item_label.pack()
item_entry = tk.Entry(window)
item_entry.pack()

quantity_label = tk.Label(window, text="Quantity: ")
quantity_label.pack()
quantity_entry = tk.Entry(window)
quantity_entry.pack()

price_label = tk.Label(window, text="Price: ")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

# Make print buttons
print_button = tk.Button(window, text="Print Receipt", bg="Red", fg="White", command=print_receipt)
print_button.pack()

# Run the main window loop
window.mainloop()

print("===========================================================================================")






        