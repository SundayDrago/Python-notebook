#these are data types which are used to store items in a single variables
# tuples are ordered an unchangeable

phone = ("samsung", "iphone", "Techno")
print(phone)

#allow for duplicate values
phone = ("samsung", "iphone", "Techno", "samsung", "Techno")
print(phone)

#Exercise use the len function

print(len(phone))
#tuples showing different data types

fruit1 = ("rice", "mango")
fruit2 = (200,300,400,500)
print(type(fruit1))
print(type(fruit2))

#Excercise, how to access tuples (negative indexing)
#by referencing the tuple index

x = [1,2,3,4,5]
print(x[0])


#2. negative indexing
x = [1,2,3,4,5]
print(x[-2])

#range of index

x = [1,2,3,4,5]
print(x[2:3])

x = [1,2,3,4,5]
print(x[:4])

x = [1,2,3,4,5]
print(x[3:])

#range of negative indexes
x = [1,2,3,4,5]
print(x[-1:-4])

#add item to the tuple
phones = ("samsung", "iphone", "Techno", "samsung", "Techno")
z = list(phones)
z.append("Nokia")
phones = tuple(z)
print(phones)

#adding two tuples

laptops = ("Del", "HP", "Acer")
laptop = ("Samsung",)

laptops += laptop
newStock =laptops + laptop

print(newStock)

print(laptops)

#using a for loop to loop through the tuple.
laptops = ("Del", "HP", "Acer")

for y in laptops:
    print(y)
