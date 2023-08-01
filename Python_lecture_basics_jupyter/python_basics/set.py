#stores multiple items in a single variable
#unchangeable but one can remove and add a new add items

set1 = {"rice", "matooke", "beans", "irish"}
print(set1)
print(type(set1))
print(len(set1))
##Duplicates in sets
''''
set1 = {"rice", "matooke", "beans", "irish", "irish"}
print(set1)
'''

##accesing items in a set
##adding items in a set, 
set = {1,2,3,4}
set.add(5)
print(set)

##Adding two sets together
setone = {1,2,3,4}                                                                                  
settwo = {5,6,7}
set_union = setone.union(settwo)
print(set_union)

#Using the update()
setone = {1,2,3,4}
settwo = {5,6,7}
setone.update(settwo)
print(setone)

#Removing set items
sets = {'mango','apple','tomato'}
sets.remove('tomato')
print(sets)

##Looping through set items
sets_items = {'banana', 'orange', 'berries', 'apple', 'pineapple'}
for y in sets_items:
    print(y)
##
##Intersection of sets
a = {"cats", "dogs", "monkey", "goat", "cows", "sheep"} 
b = {"lion", "cows", "goat", "sheep", "leopard", "gorilla"} 



