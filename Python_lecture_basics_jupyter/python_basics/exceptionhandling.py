# Python Error handling and debugging

#Exception Handling

# try:
#     a = int(input("Enter the value: "))
#     b = int(input("Enter the second value: "))
#     c = a/b
#     print(f"Answer :{c}")

# except ZeroDivisionError:
#     print("Zero division error!")

# except ValueError:
#     print("Value division error")

# except:
#     print("Unknow error")

# finally:
#     print("Success!")

#Error handling-> Error in python can be of two types, syntax errors and Exception
# Errors-> are problems in a program due to which the program will stop the execution while exception
# exception ->are raised when some internal events occur which change the normal flow of the program

# Types of exception
#->syntaxError
# TypeError
x = 19
y = "Drago"
try:
  z = x + y
  print(z)
except TypeError:
    print("Type Error")
finally:
   print("You can't continue!")
# NameError
try:
   cars =["Jeep", "v8", "Benz","Toyota"]
   
except NameError:
   print(car)
finally:
   print("Executed")

# IndexError
x = [20,30,40]
try:
   print(x[4])
except IndexError:
   print("Index is out of bound!")
# KeyError
my_dict = {'a':1, 'b':2, 'c':3}
try:
   print(my_dict['d'])
except KeyError:
   print("Key d doesn't exist in the dictionary")

#ValueError
try:
   number = int("abc")
except ValueError:
   print("Invalid value")
# AttributeError
#importError
#ZeroDivisionError




#File handling    
#Reading from a file
#Adding into an existing file
#custom exception
#