#Lists
# numbers = [1,2,3]
# numbers[0]
# Dictionary (a way to store different data points)
# Keys are unique
# Values can be any data type
# Keys can only be immutable data types
# Immutable - Strings, integers, floats, booleans 
# student_phonebook = {
#     "Cindy":111,
#     "Tracey":123,
#     "Pauline":444
#     }

#"Key":Value

# print(student_phonebook)
# del student_phonebook["Tracey"] #This delates a person from the dictionary
# print(student_phonebook)
# student_phonebook["Cindy"] = 555 #This will change Cindy's value to 555
# print(student_phonebook)
# student_phonebook["Yara"] = 555 #This adds a person to the dictionary 
# print(student_phonebook)
# print(type(student_phonebook))

# for key in student_phonebook:
#     print(key, student_phonebook[key]) #This prints the key and value

# for value in student_phonebook.values():
#     print(value) #This will print all the values 

# a,b = [1,2]
# print(a)
# print(b)

# for key,value in student_phonebook.items():
#     print(key,value)

#Exercises 

# Q1 - The dictionary below represents the cost of individual items in a supermarket. 
# Write aprogram that asks the user how many of each item they would like in turn, and outputsthe total cost of their groceries.

# groceries = {
#     "Baby Spinach": 2.78,
#     "Hot Chocolate": 3.70,
#     "Crackers": 2.10,
#     "Coffee": 9.00,
#     "Carrots": 0.56,
#     "Oranges": 3.08
#     }

#This is the long way of doing it
# spinach = int(input("How much baby spinach would you like?"))
# hotchocolate = int(input("How much hot chocolate would you like?"))
# crackers = int(input("How many crackers would you like?"))
# coffee = int(input("How much coffee would you like?"))
# carrots = int(input("How many carrots would you like?"))
# oranges = int(input("How many oranges would you like?"))

# print((spinach*2.78)+(hotchocolate*3.70)+(crackers*2.10)+(coffee*9)+(carrots*0.56)+(oranges*3.08))

#This is the short way of doing it with for loop
# totalcost = 0

# for food,price in groceries.items():
#     amount = int(input(f"How many {food}?"))
#     itemamount = amount*price
#     totalcost += itemamount #+= would mean the same as totalcost = totalcost + itemamount

# print(totalcost)

# Q2 In the last lesson, you wrote a program that counted the number of colour names in the colours_865.csv file 
# (available here).Try rewriting this program so that instead of using separate variables to keep track ofthe number of times 
# each colour name appears, it uses a single dictionary instead.Here's a dictionary to get you started:

colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
    }

with open(file="colours_20_simple.csv") as colour_file:
    csv_reader = csv.reader(colour_file)
    for colourdata in csv_reader:
        print(colourdata[3,1,0])