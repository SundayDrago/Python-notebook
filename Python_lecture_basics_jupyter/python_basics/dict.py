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
