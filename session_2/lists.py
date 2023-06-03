#Store multiple data points, can take different data types 
#str, int, float, list
# print(digits[0:5:2])
# print(list_name)
# print(type(list_name))
# print(len(digits))

#Lists are index based which starts from 0 
# print(digits[5]) #IndexError: list index out of
# print(digits[-1]) #give very last element
# print(digits[-2]) #give second last element 

#slicing a list 
#print(digits[0:4]) #start (inclusive) and end index (exclusive)
#print(digits[-2:5])

digits = [1,2,3,4,5]
# print(digits)
digits.append(6)
# print(digits)
popped_element = digits.pop(0)
# print(popped_element)
digits[1] = 90
print(digits)

#Nested list 
letters = ['a','b','c','d',['Emily','Julie']]
print(letters[4][0]) #Get the first list, then get the first element from another list


#Check if 'a' exists in list letters 
if 'a' in letters:
    print("It is in the list")