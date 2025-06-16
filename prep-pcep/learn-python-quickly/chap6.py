# conditionals if-elif else, for, while loops plus try-catch intro
#Difficulty menu if-elif-else example
difficulty = input("Choose '1' for 'Easy', '2' for 'Normal', '3' for 'Hard', or '4' for 'Expert:")
dif = int(difficulty)
if dif == 1:
    print("Easy difficulty chosen.")
elif dif == 2:
    print("Normal difficulty chosen.")
elif dif == 3:
    print("Hard difficulty chosen.")
elif dif == 4:
    print("Expert difficulty chosen.")
else:
    print("Please enter a valid difficulty.")
#How for loops are most often used in Python, to process lists and other structures
iterable = [2,4,6]
cats = ['Kitana', 'Fluffy', 'Ben', 'Cookie']
for x in iterable:
    print(x)
for cat in cats:
    print(cat + "has been fed")
#traditional for loop where you execute a counter
for a in range(0, 10):  #can also be range(0, 10, 2) where 2 is interval or step
    print("We're on beat {%d}" % (a))
#use enumerate() to retrieve index of a value
items_list = [10,9,8,7,6,5]
for index, item in enumerate(items_list):
    print(index,item)
#to loop through dictionary use key
drinks = {'drink_1':'coffee', 'drink_2':'tea'}
for i in drinks:
    print("Drink number = {}, drink = {}".format(i.drinks[i]))
# Using the items() function, which will return key and data as tuple
for i,j in drinks.items():
    print("Drink number = {}, drink = {}".format(i,j))
#loop through strings
a_string= input("Give me a string, any string!:")
for q in a_string:
    print(q)
#while loop
counter = 1
while counter <= 5:
    print("Inside while loop")
    value +=1
else:
    print("While loop over")
#Break/continue
fruit_list = ['mango', 'lemon', 'banana', 'apple', 'cherry', 'watermelon', 'orange']
for fruit in fruit_list:
    print(fruit)
    if(fruit=='apple'):
        print("Apple is in the list")
        break 
print("Loop ended")

print("Printing only odd numbers") 
num_list = [24, 46, 21, 35, 62, 12, 19, 38, 20] 
for i in num_list:
    if i%2 == 0:
        continue
    print(i)
#try/except
value = input("Enter divisor")
value = int(value)
try:
    dividend = 100/value
    print(dividend)
except:
    print("Cannot divide by zero")
#Errors
'''
ValueError - Used when a value is of the incorrect type. For instance, it can be used when a value entered by the user needs to be converted into an integer, 
    but the user has entered an incompatible string.
ZeroDivisionError - This error is triggered when trying to divide zero, which is impossible. 
ImportError - This error is triggered when Python has been instructed to import a module, but the module cannot be found or otherwise cannot be imported successfully. 
IOError - This Input/Output error notification occurs when an I/O operation cannot complete. 
    For instance, this error would trigger when an open() command is called, but the provided file cannot be found.
Index Error - This IndexError occurs when a provided sequence index is out of the range of the sequence that has been provided.
KeyError - This error is triggered when a dictionary key is provided, but the provided key does not exist or can't be found within the dictionary.
TypeError - This error occurs when some function or operation has been applied to a data type but the operation cannot be carried out successfully. 
NameError - This occurs when a designated variable name isn't found.
'''
