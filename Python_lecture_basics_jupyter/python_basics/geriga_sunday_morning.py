#DAY 3

#Basic operators and Expression (Input and Output operators)
#=============================================================================

"""
-Arithmetic Operator
+Addition
-Subtraction
*Multiplication
/Division
% modulus
**Exponentiation

-Comparison Operators
==Equal to
!== Not Equal !=
> Greater than
< Less than
>= Greater than or Equal
<= Less than or Equal

-Logical Operator
Logical AND 'and'
Logical OR 'or'
Logical NOT 'not'

-Assignment Operators
Assign value '='
Add value '+'
Add and assign value: '+='
Subtract and assign value: '-='
multiply and assign: '*='
Divide and assign value: '/=' 
Modulus and assign value: '%='
Exponentiation and assign value: '**='

-Membership Operators:
In: 'in' operator: Checks if the value exists in the varaiable
Not in: 'not in' Operator: checks if a value does not exist in a sequence

-Identity Operator:
Is: 'is' operator: checks if the two values are the same
Is not: 'is not' operator: checks if two values are not the same
"""

#Examples
#- Arithmetic Operator
#Addition

#x = 50 + 45

#print(x)
#Subtract
#y = 50 - 45

#print(y)
#Multiply
#t = 50 * 45

#print(t)
#Division
#m = 50 / 45

#print(m)
#Divide
#d = 50 // 45

#print(d)

#Modulus
#k = 50 % 45

#print(k)

#Exponentiation
#e = 50 ** 45

#print(e)


##-Comparison Operators
#==Equal to
#a=50
#b=50
#if a>b:
# print("a is equal to b")
 #print(a==b)

#!== Not Equal !=
#print(50 != 50)
#> Greater than 
#print(20>10)
#< Less than
#print(10<20)
#>= Greater than or Equal
#print(10>=20)
#<= Less than or Equal
#print(10<=20)


#Logical Operator:
#a = True
#b = False
#Logical AND
#print(a and b)

#Logical OR
#print(a or b)
#Logical NOT
#print(not b)
#print(not a)

#Assignment Operators:
#Assign value '='
#a=5
#a += 5
#print(a)
#Add and assign value: '+='
#a=90
#a +=5
#print(a)
#Subtract and assign value: '-='
#a=8
#a -=5
#print(a)
#multiply and assign: '*='
#a =14
#a *=5
#print(a)
#Divide and assign value: '/='
#t=50 
#t /=5
#print(t)
#Modulus and assign value: '%='
#y=45
#y %=5
#print(y)
#Exponentiation and assign value: '**='
#k = 7
#k **=6
#print(a)

#Members Operator:
#"cars = ['Jeep', 'BMW','v8','Roll Royce']
#"if 'Jeep' in cars:
 #print("'Jeep' is in list")
 #print('Toyota' in cars)
 #print('Primo' in cars )
 
##Identity Operators:
#x = "goat"
#y = "goat"

#print(x is y)
#print(x is not y)
#print(x == y)
#print(x != y)

#list 
#w =[1,2,3,4]
#z =[1,2,3,4]

#print(z is w)
#print(z is not w)

#Bitwise operator:
"""Bitwise operators are used to perform operations on individual in binary numbers"""

#Bitwise AND (&): Perfroms a bitwise AND operation between corresponding bits of two integer.
#Bitwise OR (|): PeRfroms a bitwise OR operation between corresponding bits of two integer.
#Bitwise XOR (^): Perfroms a bitwise XOR operation between corresponding bits of two integer.
#Bitwise NOT (~): Perfroms a bitwise NOT operation between corresponding bits of two integer.
#Bitwise left shift (<<): Perfroms a bitwise left-shift operation between corresponding bits of two integer.
#Bitwise right shift (>>): Perfroms a bitwise right-shift operation between corresponding bits of two integer.

#Example

#Bitwise and
'''
a = 10
b = 20

result_and = a & b

print(result_and)
'''


#Bitwise or
'''
a = 10
b = 20
'''


#result_and = a ~ b

#Bitwise not
'''
a = 10
b = 20

result_and = a & b

'''

#Bitwise XOR
'''
a = 10
b = 20

result_and = a ^ b
'''


#Bitwise left-shift
'''a = 10
b = 20

result_and = a << b

'''

#Bitwise right-shift
'''
a = 10
b = 20

result_and = a >> b
'''


#Example and assignment
#1. Create a simple calculator function to calculate(add, subtract, multiply, divide)
'''
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
   print("DRAGO'S SIMPLE CALCULATOR")
   number1 = float(input("Enter first number: "))
   number2 = float(input("Enter second number: "))
   operator = input("Enter the operator(+, -, *,/: )")

   if operator =='+':
      result1 = add(number1, number2)
   elif operator =='-':
      result1 = subtract(number1, number2)
   elif operator =='*':
      result1 = multiply(number1, number2)
   elif operator =='/':
      result1 = divide(number1, number2)
   else:
      print('Invalid operator')
      return
   print("The result is ", result1)

if __name__== '__main__':
      main()

   #print("Addition:", add(a, b))
   #print("Addition:", subtract(a, b))
   #print("Multiplication:", multiply(a, b))
   #print("Division:", divide(a, b))

'''
#Create a simple calculator program with aGUI interface.
#Make the ttile of the calculator program window with your name eg "GERIGA SIMPLE CALCULATOR"

import tkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_add():
    first = entry.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = int(first)
    entry.delete(0, tk.END)


def button_subtract():
    first = entry.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = int(first)
    entry.delete(0, tk.END)


def button_multiply():
    first = entry.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first)
    entry.delete(0, tk.END)


def button_divide():
    first = entry.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = int(first)
    entry.delete(0, tk.END)


def button_equal():
    second = entry.get()
    entry.delete(0, tk.END)
    if math_operation == "addition":
        entry.insert(tk.END, f_num + int(second))
    elif math_operation == "subtraction":
        entry.insert(tk.END, f_num - int(second))
    elif math_operation == "multiplication":
        entry.insert(tk.END, f_num * int(second))
    elif math_operation == "division":
        entry.insert(tk.END, f_num / int(second))


# creation of the window
window = tk.Tk()
window.title("GERIGA's SIMPLE CALCULATOR")

# Below is how to make the widgets to display the numbers and results

entry = tk.Entry(window, width=40, border=6)
entry.grid(row=0, column=0, columnspan=5, padx=11, pady=11)

# Create number values
one = tk.Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
two = tk.Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
three = tk.Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
four = tk.Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
five = tk.Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
six = tk.Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
seven = tk.Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
eight = tk.Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
nine = tk.Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
zero = tk.Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Then the operators
button_add = tk.Button(window, text="+", padx=39, pady=20, command=button_add)
button_subtract = tk.Button(window, text="-", padx=39, pady=20, command=button_subtract)
button_multiply = tk.Button(window, text="*", padx=39, pady=20, command=button_multiply)
button_divide = tk.Button(window, text="/", padx=39, pady=20, command=button_divide)

# Create a clear button
button_clear = tk.Button(window, text="Clear", padx=83, pady=20, command=button_clear)

# Lastly, the equal button
button_equal = tk.Button(window, text="=", padx=93, pady=23, command=button_equal)

# Append the buttons to the grid
one.grid(row=3, column=0)
two.grid(row=3, column=1)
three.grid(row=3, column=2)

four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)

seven.grid(row=1, column=0)
eight.grid(row=1, column=1)
nine.grid(row=1, column=2)

zero.grid(row=4, column=0)

# =============================================================
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# For starting the main event
window.mainloop()
