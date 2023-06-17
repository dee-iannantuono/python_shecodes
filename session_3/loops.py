# Loops help us to perform tasks multiple times
# letters = ['a','b','c']

# 2 Types of loops

# While Loops
# count = 0
# while 5 > 1:
#     print("Hello")
#     count = count + 1 

# name = input("What is your name?")
# while name != "Ashley":
#     print("I don't know you")
#     name = input("Well, what's the new name?")

# For loops
# letters = ['a','b','c']
# for letter in letters: # letter = 'a'
#     print(letter)

# list_name[0:10] range() is similar to 
# for number in range(0,10):
#     print(number)

# students = [
#     ["Cindy","Emily","Eve"],
#     ["Julie","Maddy","Andrea"],
#     ["Jenny","Sarah","Yara"]
#     ]
# for student in students:
#     print(student)
#     for name in student:
#         print(name)

# Exercises 

#Q1  += will make a sum and then continue to add numbers 
# sum = 0
# number = input("Enter a number")
# while number != '':
#     sum += int(number) 
#     number = input("Enter a number")
# print(f"Your numbers sum to {sum}")

# #With list option
# number = input("Enter a number")
# number_list = []
# while number != '':
#     number_list.append(int(number))
#     number = input("Enter another number")
# if number == '':
#     print(f"Your numbers sum to {sum(number_list)}")

#Q2 option 1
# print("The first number is 0")
# large_number = int(input("Enter a number:"))
# while (large_number > 0):
#     if(large_number % 2 != 0):
#         print(large_number)
#         large_number = large_number - 1
#     else:
#         large_number = large_number -1


#Q2 option 2
# number=0
# integer_number= int(input("Please enter a number"))

# while number <= integer_number:
#     if number % 2 == 1:
#         print(number)
#     number = number+1

#Q3 
# print("Guess the random number!")
# number = 76
# guess_attempt = input("Make a guess!")

# while(True):
#     if int(guess_attempt) < number:
#         print("Too low")
#         guess_attempt = input("Make another attempt")
#     elif int(guess_attempt) > number:
#         print("Too high...")
#         guess_attempt = input("Make another attempt")
#     elif int(guess_attempt) == number:
#         print("You get it right!")
#         break

#FOR Loop exercises 
#Q1 Ask the user for a number. Use a for loop to print the times tables for that number,up to ten:

# to_multiply = int(input("Give me a number"))
# for number in range(1,11):
#     print(f"{to_multiply} x {number} = {to_multiply*number}")

#Q2 Ask the user for an integer. Using a for loop, add up every number from 0 up to thatinteger, and print the result

# user_number = int(input("Enter a number"))

# for number in range (0, user_number+1):
#     number = number + number
#     print(number)

# print(str(number))

#Q3 Save a list of numbers to a variable in your script, and then use a for loop to print thesum of all the numbers in the list

# my_numbers = [3, 5, 9, 1]
# total = 0
# for element in my_numbers:
#     total = total + element
# print(total)

# Q4 Let's improve our Mambo No. 5 code from the last block of content

# lyrics = [
#     ["Monica", "in my life"],
#     ["Erica", "by my side"],    
#     ["Rita's", "all I need"],    
#     ["Tina's", "what I see"],    
#     ["Sandra", "in the sun"],    
#     ["Mary", "having fun"],    
#     ["Jessica", "here I am"]
#     ]

# for i in lyrics:
#     name = i[0]
#     text = i[1]
#     song = "A little bit of " + name + " " + text + ";"
#     print(song)
# print(f"A little bit of you makes me your man (ah!)")
# print(f"*trumpet solo")

# for i in lyrics:
#     name, text = i #This works as well and makes it shorted
#     song = "A little bit of " + name + " " + text + ";"
#     print(song)
# print(f"A little bit of you makes me your man (ah!)")
# print(f"*trumpet solo")

# Nested Loops 
# Q1

# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["BBQ Shapes", 9.00],
#     ["Bread", 2.10],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
#     ]

# sum = 0 

# for food,price in groceries:
#     amount = int(input(f"Please enter the quantity for {food}"))
#     itemamount = amount*price
#     sum = sum + itemamount 

# print(f"Thank you, your total is ${sum}")