#Boolean
# name = "Dee"
# age = 28
# height = 1.65
# is_raining = True
# my_variable2 = False
# print(is_raining)
# print(type(is_raining))

#Boolean Expressions - Expressions that produce a boolean variable
# == checks if 2 things you are comparing is equal 
# != checks if it is not equal 
# > greater than
# < less than 
# >= greater or equal to 
# <= less than or equal to 

# print(5 > 3)
# print(3.5 > 6.3)
# print("Dee" == "Dee")

#Mathematical Operators - Addition, Division, Subtraction, Multiplication 
#Boolean Operators - not, and, or

# is_sunny = True
# is_warm = True
# print(not is_sunny)
# print(is_sunny and is_warm)
# print(is_sunny or is_warm)

#elif = if you have multiple if statements, and you only want it to check the fisrst then use IF then ELIF. Multiple IF statements will check the if statements regardless. 

# temperature = 20
# # syntax / semantics
# if temperature < 18:
#     print("Weather is too cold!")
#     print("I want to stay home")
# elif temperature > 28:
#     print("Weather is too hot!")
# else:
#     print("Weather is nice!")
#     print("Weather is nice!")
# print("My dog looks cute")

# Exercises below

#Q1 - SUCCESS

# sara_has_helmet = True

# if sara_has_helmet:
#     print("Let's send it!")
# else:
#     print("No way, my brain is my moneymaker!")

#Q2 - SUCCESS

# sara_has_helmet = False
# rei_has_rope = False

# if sara_has_helmet and rei_has_rope:
#     print("Let's send it!")
# elif sara_has_helmet:
#     print("Who's unprepared now, Rei??")
# elif rei_has_rope:
#     print("No way, my brain is my moneymaker!")
# else:
#     print("I guess let's just go hiking")

#Q3 - SUCCESS

# light_color = "Amber"
# car_detected = True

# if light_color == "Red" and car_detected:
#     print("Flash!")
# else:
#     print("Do nothing")

# Q4

input("What is your height?")

if input <= 50:
    print("Hop on!")