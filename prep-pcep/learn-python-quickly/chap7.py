#functions, modules, paths for file access
'''
Normal global variables are simply declared outside functions.
Use the global keyword to declare a global variable inside function.
However the function must first be called before a global variable defined inside can be accessed.
'''
def multiply_values(num_1, num_2):
    global ubiq
    ubiq = "free radical"
    return num_1 * num_2

def use_default_param(var_1, var_2=9):      #default parameters
    print("Value 1 is: " + str(var_1))
    print("Value 2 is: " + str(var_2))

def use_args(*sentences):               #*args when you have an indefinite number of arguments
    for sentence in sentences: 
        print(sentence)

def use_kwargs(**emails):               #*kwargs when you have a dictionary
    for k, val in emails.items(): 
        print("Name = {}, email = {}".format(k, val))
        print(f"Name = {k}, email = {val}")

print(f"Product of multiplication is {multiply_values(9, 6)} plus {ubiq}")
use_default_param(7)
use_args("This is sentence 1", "This is sentence 2", "This is sentence 3", "This is sentence n")
use_kwargs(a='joebrown@test.com', b='johndoe@test.com', c='mikelee@test.com')
# import and use built-in module
import random as r
print(r.random())
# import and use custom module. divmod.py is in same path
import divmod as dv     #import custom module divmod.py with alias dv
print(f"The results are {dv.divmod_func(3,3)} and {dv.div_by_3(9)}") # call divmod_func and div_by_3
# import and use custom module. divmodrel.py is in different path. requires sys.path.append and os
import sys
import os
#this is relative path. 'testmod' is one directory up. '..' is one directory down
sys.path.append(os.path.join(os.path.dirname(__file__), 'testmod')) 

# Now you can import modules from the 'my_modules' directory
import divmodcp as dvcp
print(f"The results are {dvcp.divmod_func(3,3)} and {dvcp.div_by_3(9)}")

#this is full path
sys.path.append(os.path.join(os.path.dirname(__file__), '/home/username/learnpy/prep-pcep/learn-python-quickly/testmod2'))
import divmodcp2 as dvcp2 
print(f"The results are {dvcp2.divmod_func(3,3)} and {dvcp2.div_by_3(9)}")

#string methods
'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Converts the elements of an iterable into a string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''
#list and array methods
'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''
#dictionary methods
'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''