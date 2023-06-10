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

#Loop exercises 
#Q1

# to_multiply = int(input("Give me a number"))
# for number in range(1,11):
#     print(f"{to_multiply} x {number} = {to_multiply*number}")

#Q2

user_number = int(input("Enter a number"))

for number in range (0, user_number+1):
    number = number + number
    print(number)

print(str(number))