#=============================================
#use to determine the truth or false nature of a statement

print(20>30)
print(10==10)
print(20<30)
##print a message base on the whether the condition is true or false

a = 30
b = 20

if b > a:
    print("b is greater than a")
else:
    print('b is less than a')

##Evaluate values and variables
print(bool("Hello"))
print(bool(15))

##Declaring values
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

##Exercise: Give an example to to use boolean values and conditions to control program flow
#This program sows if a student is eligible for sponsorship based on their grades and attendance

min_grades = 80

min_attendance_percentage = 90
student_name = input("Enter the student's name: ")
grade = float(input("Enter the student's grade: "))
attendance_percentage = float(input("Enter student's attendance percentage: "))


#use control flow statements like 'if'

if grade >=min_grades and attendance_percentage >= min_attendance_percentage:
    print(f"Congratulations!, {student_name}! You are eligible for our sponsorship ")
elif grade <= min_grades:
    print(f"{student_name}! Your grade is below the minimum required grades!")

elif attendance_percentage >= min_attendance_percentage:
    print(f"{student_name}! Your attendance is below the minimum required attendance!")
else:
    print(f"{student_name}! You are not eligible for our sponsorship! Thank you")

    #=====================================

    #used to store data values in key:value pairs
#

mydict = {

"phone": "iphone",
"year": 2023,
"iphonemodel": "iphone15"

}
print(mydict)

#dictionary length
print(len(mydict))

#datatypes
print(type(mydict))

#how to acess dictionary items
#forexample accessing the year
z = mydict["year"]
print(z)


#using getter
y = mydict.get("iphonemodel")
print(y)
#the key's method
w = mydict.keys()
print(w) ##to access the keys not values

dicts = {
    "christian": "Bible",
    "Islam": "Qu'ran"
}

#printing the details
print(dicts)

#using the getter
t = dicts.get("christian")
print(t)

#exercise one: use the values () method to return all the values in the diction
items ={
    "christian": "Bible",
    "Islam": "Qu'ran"
}
y = items.values()
print(y)
#exercise two: Give an example on how to check if the key exists in the dictionary 
items ={
    "christian": "Bible",
    "Islam": "Qu'ran"
}
if "pegan" in items:
    print(items)
else:
    print("key 'pegan' doesnt exist")
#exercise three: Give an example on how to change dictionary items, how to update.
my_dictionary = {'apple':1, 'grape':2, 'orange':3}

#change item by key
my_dictionary['apple'] = 6
print(my_dictionary)
#using update
my_dictionary.update({'grape':7, 'orange':8})
print(my_dictionary)
#exercise four: Give an example on how to add dictionary items, how to remove dictionary items
book ={
    "Title": "To Kill a mockingbird",
    "Author": "Harper Lee",
    "Pulbisher": "J.B.Lippincott & Co."
}
book["color"]="Green"
book["Year"]="1960"

print(book)

#Give an example on how to loop throug a dictionary items and also how to nest dictionaries
##1. Loop through the diction
dict_loop = {
    "christian": "Bible",
    "Islam": "Qu'ran"
}
for key, value in dict_loop.items():
    print(key, value)

##2. HOW TO NEST DICTIONARIES
mycourse = {
 "yearone" :{
     "SemOne":{"Information_system" : 3,
     "Software_Engineering_Mathematics": 4,
     "Computer_Literacy" : 4,
     "Technical_Analysis": 4
     },
     "SemTwo":{
    "OOP" : 3,
     "Numerica_Analysis": 4,
     "WebDevelopment" : 4,
     "DIM": 4
     }
      },
    "yearTwo" :{
     "SemOne":{
    "ComputerNetwork" : 3,
     "Data_Structure_And_Algorithms": 4,
     "OOP-2" : 4,
     "Artificial_Intelligence": 4
     },
     "SemTwo":{
    "Operating_System" : 4,
     "Requirements_Engine4ring": 3,
     "Emerging Web Programming" : 4,
     "Data_Communication": 4,
     "Mobile App Programming":4
     }
    }

}

#print(mycourse)# Prints all the items in the dictionary

#to access the items in the  year two
print(mycourse["yearTwo"])

#==========================================
#focus on integers, floats, and complex numbers
'''
w = 10 #integer
y = 12.33 #floats
s = 2j #complex number

print(type(w))
print(type(y))
print(type(s))


#integers
a = 2
b = -122344
c = 43637272

print(type(a))
print(type(b))
print(type(c))

#floats
a = 2.0
b = -122.344
c = 436.37272

print(type(a))
print(type(b))
print(type(c))


#complex number
a = 2.0j
b = 2+4j
c = -2j
print(type(a))
print(type(b))
print(type(c))
#type conversion

 '''
r= 10
w = 1.2
t = -2j

#convert from int to complex

z = complex (r)
print(z)
print(type(z))

#convert from complex to int
r= 10
w = 1.2
t = -2j

k = int (t.imag)
print(z)
print(type(z))

#Exercise: perform an arithmetic operations and print the results

num1 = 10
num2 = 20

#addition
add = num1 + num2

print(add)

#subtraction
sub = num1 - num2

print(sub)


#multiplication
multiply = num1 * num2

print(multiply)


#division
divide = num1 / num2

print(divide)

#floor division
floor_division = num1 // num2

print(floor_division)

#modulo
modulas = num1 % num2

print(modulas)

#exponentiation
exponentiation = num1 ** num2

print(exponentiation)

#=============================================================
"""
# Enclose in double quotes or single quotes
print("Afternoon")
print('Afternoon')

#assign string to variable
w = 'afternoon'
print(w)

##multi-line string

o = """
#I am not hungry
#I am in year 3
#I am doing recess
"""
print(o)

#concatenate
w = "Paul"

y = "Tandrupasi"

z = w + " " + y
print(z)

"""

#Exercise one: the len() function to determine the length of your string
#Strip = """
#I am not hungry
#I am in year 3
#I am doing recess
#"""
#print(len(Strip))

#Exercise Two: Give an example of using a loop in string

loop_string = "Hoola!, Geriga"

for char in loop_string:
    ##Therefore, convert the characters to upper
    #uppercase_char = char.upper()
    #print(uppercase_char)

    """ Output:
    H
    O
    O
    L
    A
    ,
    G
    E
    R
    I
    G
    A
    """

#Exercise Three: Give an example on slicing in strings
mystring = "HOW TO REVERSE A STRING!"

#slicing the string from the beging
substring1 = mystring[:5]

print(substring1)

#slicing till the end 
substring2 =mystring[9:]
print(substring2)


#slicing with step values

substring3 =mystring[::3]
print(substring3)


#reversing a string using slicing
reversed_string = mystring[::-1]

print(reversed_string)





