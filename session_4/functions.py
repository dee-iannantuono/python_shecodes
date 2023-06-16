# Function - an activity that is natural to or the purpose of a person or thing. 
# Functions we've already seen
#input(),len(),int(),print() 

# name = input("What is your name?")
# age = input("How old are you?")
# if age >= 18:
#     print("Welcome")
# else:
#     print("You can not enter.")

#Task Seperation
# def ask_user_name():
#     # print("Now function is entered")
#     name = input("What is your name?")
#     # print(name)
#     return name

#Function definition
#Calling a function

# print("hello")
# answer = ask_user_name() #user_input = input("tell me your name")
# print("Hi")

# def ask_user_age():
#     age = input("How old are you?")
#     if age >= 18:
#         print("Welcome")
#     else:
#         print("You can not enter.")


# Parameters
# def add(number1, number2): #number1 = 2, number2 = 3
#     result = number1 + number2
#     return result

# answer = add(2,3) 
# print(answer)
# print(result) #local variable


#Global/Local Variables



#Exercises 

#Q1
#Write a function called get_integer that takes a string as its argument, and uses thatstring to prompt the user to enter an integer.
#Your function should return the integersupplied by the user

# prompt = "Could i please have an integer?:"

#Define your function here

# def get_integer():
#     user_input = int(input("Could i please have an integer"))
#     print(f"so your integer is {user_input}? Thanks!")


#Q2
#Write a function called celcius_convert that takes a number representing thetemperature
#in Farenheit as its argument, and returns a float representing thetemperature in Celcius

#Divide by 5, then multiply by 9, then add 32


# fahrenheit = 35
# celcius_convert = fahrenheit - 32 * 5 % 9
# print(f("{celcius_convert}"))

# def celcius_convert():
#     celcius_convert = {{degrees_f}-32}*{5/9}

# degrees_f = celcius_convert(5,9,32)
# print((degrees_f))




# weight="47.6"
# print(type(weight))
# print(f("My weight is {weight*2.1}in lbs"))