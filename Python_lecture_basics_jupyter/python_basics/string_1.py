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

