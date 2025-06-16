# Lists are mutable
tasks = ["Buy groceries", "Finish report", "Call Mom"]

# tuples are immutable
my_tuple = (10, 20, "python")

# sets only store unique unordered item 
my_set = {1, 2, 3, 3} 

print(my_set)  # Output: {1, 2, 3}
# Unordered Nature: Since sets are unordered, you can't rely on the position of elements. 
# This means you can't access elements by index (like my_set[0]) as you would with a list.

# Key Operations: Sets are designed for efficient operations involving unique elements. You can easily:
# add() new elements to a set.
# remove() elements from a set.
# union() Find the union() of two sets (all elements from both sets).
# intersection() Find the intersection() of two sets (elements common to both sets).
# difference() Find the difference() between two sets (elements in one set but not the other).

# dictionary: key-value pairs
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing values: To retrieve a value from the dictionary, you use its associated key. 
# In our example, my_dict["age"] would return the value 30.

# Mutability and flexibility: Dictionaries are dynamic structures. 
# You can add new key-value pairs, modify the values associated with existing keys, or even remove pairs altogether. 
# This adaptability makes dictionaries suitable for a wide range of applications where data needs to be updated or changed over time.

# Common operations: Dictionaries offer a variety of convenient methods for working with key-value pairs:
# get(): Safely retrieve a value by its key (returns None if the key doesn't exist).
# items(): Get all key-value pairs as a list of tuples.
# keys(): Get all keys in the dictionary.
# values(): Get all values in the dictionary.
# update(): Merge another dictionary into the existing one.


# dictionary that includes dictionaries as value in key value pairs (below the keys are P101, P102, Pxxx)
products = {

		"P101": {"name": "Laptop", "price": 999.99},

		"P102": {"name": "Smartphone", "price": 599.99}

		}

# Contact information dictionary with email address as tuple (immutable) and a dictionary with name, grade and phone as key pairs
alice_dict = {('alice@example.com'):{"name":'Alice', "grade":85, "phone":'123-456-7890'}}