grocery_list = ["milk", "hummus", "bread", "cheese", "apples"]
x = "steak"
i = 3

len(grocery_list)           #Returns the number of items in the list. For example, len(grocery_list) would be 5.

grocery_list.append(x)      #Adds x to the end of the list. 
                            #For example, grocery_list.append("bananas") would add "bananas" to the end of our grocery list.

grocery_list.insert(i, x)   #Inserts x at index i in the list. 
#For example, grocery_list.insert(1, "yogurt") would add "yogurt" at index 1, shifting "hummus" and the other items to the right.

grocery_list.remove(x)      #Removes the first occurrence of x from the list. 
#For example, if we accidentally added "milk" twice, grocery_list.remove("milk") would remove the first occurrence.

grocery_list.sort()         #Sorts the items in the list in ascending order. 
#For example, numbers.sort() would arrange the numbers from smallest to largest, or strings in alphabetical order. 
#However, keep in mind that you can only sort lists that contain all numbers or all strings, not a mix of different types!

grocery_list.reverse()      #Reverses the order of items in the list. 
#For example, if we have numbers = [1, 2, 3], then numbers.reverse() would make it [3, 2, 1].

grocery_list.count(x)       #Counts how many times x appears in the list. 
#For example, if we have letters = ["a", "b", "a", "c", "a"], then letters.count("a") would return 3.

grocery_list.index(x)       #Tells you the position of the first x in the list.

grocery_list.pop()          #Removes and returns the last item in the list, similar to crossing off the final task on your list.

del grocery_list            #deletes lists and other mutable objects, variables or specific elements within mutable data structures like lists and dicts

if x in grocery_list:       #Checks if x is in the list.
    print(f"{x} is here")

# Create an empty list to represent the shopping cart
shopping_cart = []

# Add items to the shopping cart
shopping_cart.append("apple")
shopping_cart.append("banana")
shopping_cart.append("milk")

# Print the contents of the shopping cart
for item in shopping_cart:
    print(item)

# Create a dictionary to store contact information
contacts = {"Alice": "555-1234", "Bob": "555-5678", "Carol": "555-9012"}

# Look up Bob's phone number
bobs_phone = contacts["Bob"]
print(bobs_phone)
# Output: 555-5678

# Add a new contact
contacts["David"] = "555-4321"

# Update Carol's phone number
contacts["Carol"] = "555-2468"

# Remove Alice's contact information
del contacts["Alice"]

# Print updated contacts
print(contacts)