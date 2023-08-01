afternoon = ["Trevor", "Peter", "Blessing"]
#print(afternoon)
#duplicates in the list

afternoon =["Trevor", "Peter", "Blessing", "Trevor", "Trevor", "Blessing"]
print(afternoon)
#list length
print(len(afternoon))
#type
print(type(afternoon))

#acessing the list items
print(afternoon[4])

print(afternoon[-3])

print(afternoon[1:3])
print(afternoon[1:])
print(afternoon[:4])

#adding list item  append

afternoon.append("Geriga")
print(afternoon)



#adding list item using insert

afternoon.insert(0, "Livingstone")
print(afternoon)

#removing list items
afternoon.remove("Livingstone")
print(afternoon)

afternoon.pop(6)
print(afternoon)