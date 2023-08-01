# DAY 3 LECTURE

print("========================Exercise One===================================")
# Question one
lists = ['Andrew', 'John', 'Sandra', 'Beatrice']

print(lists[1])
print("--------------------------------------------------------------------")
# Question two

lists = ['Andrew', 'John', 'Sandra', 'Beatrice']
lists[0] = "Paul"
print(lists)
print("--------------------------------------------------------------------")
# Question three
lists = ['Andrew', 'John', 'Sandra', 'Beatrice']
lists.insert(6, "Martha")

print(lists)
print("--------------------------------------------------------------------")
# Question 4
lists = ['Andrew', 'John', 'Sandra', 'Beatrice']
lists.insert(2, "Bathel")
print(lists)
print("--------------------------------------------------------------------")
# Question 5
lists = ['Andrew', 'John', 'Sandra', 'Beatrice']
lists.remove("Sandra")
print(lists)
print("--------------------------------------------------------------------")
# Question 6
lists = ['Andrew', 'John', 'Sandra', 'Beatrice']
print(lists[-1:])
print("--------------------------------------------------------------------")
# Question 7
lists = ['Andrew', 'John', 'Sandra', 'Beatrice', "Drago", "Iraku", "Atong"]
print(lists[2:5])
print("--------------------------------------------------------------------")
# Question 8
countries = ['Uganda', 'Kenya', 'Tanzania', 'Congo', 'Somalia']
country_co = countries.copy()
print(countries)
print(country_co)
print("--------------------------------------------------------------------")
# Question 9
countries = ['Uganda', 'Kenya', 'Tanzania', 'Congo', 'Somalia']
for count in countries:
    print(count)
print("--------------------------------------------------------------------")
# Question 10
animals = ['cat', 'dog', 'goat', 'cow', 'sheep']
ascending_order = sorted(animals)
descending_order = sorted(animals, reverse=True)

print("Original list of animals: ", animals)
print("--------------------------------------------------------------------")
print("Sorted in ascending order", ascending_order)
print("--------------------------------------------------------------------")
print("Sorted in descending order", descending_order)
print("--------------------------------------------------------------------")
# Question 11
animals = ['cat', 'dog', 'goat', 'cow', 'sheep']
for animal in animals:
    if 'a' in animal:
        print(animal)
print("--------------------------------------------------------------------")
# Question 12
first_names = ["Iraku", "Geriga", "Namutamba", "Atong", "Ngong"]
second_name = ["Harry", "Sunday", "Dorothy", "Abraham", "Abraham"]

full_name = []
for first_names, second_name in zip(first_names, second_name):
    full_name.append(first_names + " " + second_name)

    print("Full Name: ")
    for name in full_name:
        print(name)
print("--------------------------------------------------------------------")
# ======================================
print("==============================Exercise Two===============================================")
# Question One
x = ("Samsung", "iphone", "techno", "redmi")
favorite_phone = x[1]

print(favorite_phone)
print("--------------------------------------------------------------------")
# Question Two
second_last_item = x[-2]
print(second_last_item)
print("--------------------------------------------------------------------")
# Question Three
x_list = list(x)
index = x_list.index("iphone")
x_list[1] = "itel"
x_updated = tuple(x_list)
print(x_updated)
print("--------------------------------------------------------------------")
# Question Four
x = ("Samsung", "iphone", "techno", "redmi")
x_list = list(x)
x_list.append("Huawei")
x_updated = tuple(x_list)
print(x_list)
print("--------------------------------------------------------------------")
# Question Five
x = ("Samsung", "iphone", "techno", "redmi")
for phones in x:
    print(x)
print("--------------------------------------------------------------------")
# Question Six
x = ("Samsung", "iphone", "techno", "redmi")
x_list = list(x)
x_list.pop(0)

x_update = tuple(x_list)

print(x_update)
print("--------------------------------------------------------------------")
# Question Seven
cities = tuple(["Kampala", "Gulu", "Entebbe", "Jinja", "Masaka"])

print(cities)
print("--------------------------------------------------------------------")
# Question Eight
# To unpack the cities
cities = tuple(["Kampala", "Gulu", "Entebbe", "Jinja"])
city_one, city_two, city_three, city_four = cities
print(city_one)
print(city_two)
print(city_three)
print(city_four)
print("--------------------------------------------------------------------")
# Question nine
cities = tuple(["Kampala", "Gulu", "Entebbe", "Jinja"])
rang = cities[1:4]

print(rang)
print("--------------------------------------------------------------------")
# Question ten
first_names = ("Iraku", "Geriga", "Namutamba", "Atong", "Ngong")
second_name = ("Harry", "Sunday", "Dorothy", "Abraham", "Abraham")
full = first_names + second_name
print(full)
print("--------------------------------------------------------------------")
# Question eleven
color = ("Red", "Blue", "Pink", "Yellow")
multiply_color = color * 3
print(multiply_color)
print("--------------------------------------------------------------------")
# Question Twelve
numbers = (1, 2, 4, 6, 2, 5, 8, 5, 8, 2, 0)
counter = 0
for number in numbers:
    if number == 8:
        counter = counter + 1
print(counter)


# =====================================
# Exercise 3
print("==========================Exercise Three==============================================")
# Question 1
beverages = {"Cococola", "Fanta", "Sting"}
print(beverages)
print("=======================")
print("--------------------------------------------------------------------------")
# Question 2
beverages = {"Cococola", "Fanta", "Sting"}
beverages.add("Energy-X")
beverages.add("Owner")
print(beverages)
print("=======================")
print("-------------------------------------------------------------------------")
# Question 3
myset = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in myset:
    print("microwave" in myset)
print("=======================")

# Question 3
myset = {"oven", "kettle", "microwave", "refrigerator"}
myset.remove("kettle")

print(myset)
print("=======================")

# Question 5
nyiset = {"oven", "kettle", "microwave", "refrigerator"}

for kit in nyiset:
    print(kit)
print("--------------------------------------------------------------------")

# Question 6
item = {"cup", "plate", "pan", "stove"}
itemz = ["posho", "beans", "meat", "eggs"]
print("--------------------------------------------------------------------")
item.update(itemz)
print(item)
print("--------------------------------------------------------------------")

# Question 7
first = {"Iraku", "Geriga", "Namutamba", "Atong", "Ngong"}
ages = {23, 18, 15, 34, 19}
first.update(ages)
print(first)
print("--------------------------------------------------------------------")
#
print("=================================Exercise 4===========================================")
# Question 1
statement = "You are "
year = 25
conc = statement + str(year) + "years old"
print(conc)
# =======================================
print("--------------------------------------------------------------------")
# Question 2
txt = " Hello, Uganda! "
output = txt.strip()
print(txt)
print("--------------------------------------------------------------------")
# Question 3
txt = " Hello, Uganda! "
text = txt.upper()
print(text)
print("--------------------------------------------------------------------")
# Question 4
txt = " Hello, Uganda! "
tex = txt.replace('U', 'V')
print(tex)
print("--------------------------------------------------------------------")
# Question 5

Y = "I am proudly Uganda"
range_of_character = Y[1:4]
print(range_of_character)
print("--------------------------------------------------------------------")
# 6
x = 'All "Data Scientist" are cool'
x = x.replace('"', '\"')
print(x)

#
print("====================================Exercise Five============================================")
# Exercise 5
print("Exercise 5")
shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(shoes)
print("--------------------------------------------------------------------")

# Question 2
shoes["brand"] = "Adidas"
print(shoes)
print("--------------------------------------------------------------------")
# Question 3
shoes["types"] = "sneaker"
print(shoes)
print("--------------------------------------------------------------------")
# Question 4
key = shoes.keys()
print(key)
print("--------------------------------------------------------------------")
# Question 5
value = shoes.values()
print(value)
print("--------------------------------------------------------------------")
# Question 6
if 'size' in shoes:
    print("The key 'size' is exists in the dictionary")
else:
    print("The key 'size' does not exist in the dictionary")
print("--------------------------------------------------------------------")
# Question 7
for key, value in shoes.items():
    print(f"The key is {key} and the value is {value}.")
print("--------------------------------------------------------------------")
# Question 8
del shoes["color"]
print(shoes)
print("--------------------------------------------------------------------")
# Question 9
shoes.clear()
print(shoes)
print("--------------------------------------------------------------------")
# Question 10
my_diction = {
    "name": "John",
    "age": 30,
    "occupation": "software Engineer"
}
copy_dict = my_diction.copy()
print(copy_dict)

# Question11
my_course = {
    "year-one": {
        "Sem-One": {"Information_system": 3,
                   "Software_Engineering_Mathematics": 4,
                   "Computer_Literacy": 4,
                   "Technical_Analysis": 4
                   },
        "Sem-Two": {
            "OOP": 3,
            "Numerica_Analysis": 4,
            "WebDevelopment": 4,
            "DIM": 4
        }
    },
    "year-Two": {
        "Sem-One": {
            "ComputerNetwork": 3,
            "Data_Structure_And_Algorithms": 4,
            "OOP-2": 4,
            "Artificial_Intelligence": 4
        },
        "Sem-Two": {
            "Operating_System": 4,
            "Requirements_Engine4ring": 3,
            "Emerging Web Programming": 4,
            "Data_Communication": 4,
            "Mobile App Programming": 4
        }
    }

}

# print(mycourse)
# # Prints all the items in the dictionary

# to access the items in the  year two
print(my_course["year-Two"])
print("--------------------------------------------------------------------")