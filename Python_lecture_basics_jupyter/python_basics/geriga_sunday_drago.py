#Running Python Scripts

print('GERIGA SUNDAY DRAGO')

print("GERIGA SUNDAY DRAGO")
#PEP8: Python Scripts Guidelines    

'''
1.Indentation
2.Line of character shouldn't go 79
3.whitespace
4.Naming convention (CamelCase, snake_case)
5.comment(
   i).multi-line-comments(''''''), 
  ii).single-line-comments(#))
'''
#Variable
'''
name = "Geriga"
age = 23
print('Name: ',name)
print('Age :',age)
'''

#data structures (data-types)
'''Numeric values
  types of numerics (integers, floats)

  string values are str
  can be represented as 'Geriga' or 'Sunday'

  boolean values represent logic (true or false)

  sequence types can be inform of 
  i)lists ->can be enclose with square brackets [] -> in ordered collections
  ii)tuples ->enclosed with parenthesis()
  iii) range ->often used in iterations, loops

  Mapping types 
  1.dict ->dictionary is enclosed with curly braces {}

  example 
  {
  name : 'Geriga'
  age : 27
  }
  or {name :'Geriga', age : 27}

  2.set Types represented in unordered way, unique
   
  3. None Types: None represents absence of a value
  name: name
'''

'''
gen_gender_sex =False

print(gen_gender_sex)
'''

"""
list -> they are used to store many items in a variable
lists are ordered , changeable, allow duplicate values
"""

##if condition
##if gen_gender_sex:
#    print("male")
#else:
 #   print("female")

#example 1
# age <18, print "You are underage"
'''
age = 70

if age <18:
    print("You are underage")
elif age >=18 and age<=65:
    print("You are a adult")
else:
    print("You are a senior adult")

#loops
#we have two loops->for loop, while loops
for i in squence:
loop through
4

cars = ["tesla", "jeep", "toyota"]

for car in cars:
    print(car)

fruits = ["Orange", "Banana", "Pineapple"]

for fruit in fruits:
    print(fruits)
'''

#while loop
'''
fruits = ["Orange", "Banana", "Pineapple"]
fruit_count =0
while fruit_count <len(fruits):
    print(fruits(fruit_count))
    fruit_count +=1
    

    ##exercise on loops
    i = 1

while i < 6:
    print(i)
    i += 1
    if i == 3:
        continue
#break and continue

#break statement
for number in  range(1,10):
    if number == 5:
        break
    print(number)

 
for number in  range(1,10):
    if number == 5:
        continue
    print(number)

      
names =["John", "Paul","Joel","Paska"]

for name in names:
    if name == "Joel":
        continue
    print(name)


names =["John", "Paul","Joel","Paska"]

for name in names:
    if name == "Joel":
        break
    print(name)
 
 #exception handling
 #example
try:
 x=10/0
except ZeroDivisionError:
   print('Error: Division by Zero')
finally:
  print('This is always exceuted')

#example 5
#a dictionary{}

emotion = {
  'happy' : " I'm glad to hear you're happy",
  'sad' : "I'm sorry to hear that you are feeling sad",
  'angry' : "You will be fine",
  'fearful' : "I understand that fear can be challenging",
  'disgusted' : "To feel disgusted is really good"
}

user_emotion = input("How are you feelig today")
user_emotion = user_emotion.lower()
if user_emotion in emotion:
    print(emotion[user_emotion])
else:
    print("I'm sorry, i don't understand your emotions")
'''
    #Exercise:
#WRITE A PROGRAM TO ASK STUDENTS ABOUT THEIR MENTAL HEALTH
#prompt students on a scale of 1 to 10 to rate their mental health

'''
#
student_name = input("Enter you name: ")

while True:  
    try:
        rating = int(input("On scale of 1 to 10, rate your mental health: "))
        if 1 <= rating <=10:
            break
        else:
            print("Please enter a rating between 1 and 10!")
    except ValueError:
        print("Invalide input, Please enter a number")

print(f"Thank you, {student_name}! You rated your mental health as {rating}/10.")
  '''
#
