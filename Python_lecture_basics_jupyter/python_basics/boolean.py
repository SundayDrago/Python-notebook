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