# sets only store unique unordered item 
my_set = {1, 2, 3, 3}
other_set = {6, 7, 8, 8} 
item = 9 

#Key characteristics
#Unordered: The order in which you add items to a set is not preserved. Like your stamp collection, 
# the arrangement doesn't matter as long as you can quickly determine if a specific stamp is part of it.

#Mutable: Sets are dynamic. You can add new items to a set or remove existing ones,
#  just as you might acquire new stamps or trade duplicates with other collectors.

#Unique: This is the defining feature of sets. Each item can appear only once within a set, mirroring the uniqueness of each stamp in your collection.

#Common operations
my_set.add(item) #Adds the item to the set only if it's not already present.

my_set.remove(item) #Removes the item from the set if it exists.

my_set.union(other_set) #Combines two sets to create a new set containing all unique elements from both.

my_set.intersection(other_set) #Creates a new set containing only the elements that are common to both sets.

my_set.difference(other_set) #Creates a new set containing elements that are in the first set but not in the second.

my_set.issubset(other_set) #Checks if all elements of the first set are also in the second set.

my_set.issuperset(other_set) #Checks if all elements of the second set are also in the first set.

# Create a set of favorite programming languages
languages = {"Python", "JavaScript", "Java"}
# Add "C++" to the set
languages.add("C++")
# Try to add "Python" again (it won't be added because it's a duplicate)
languages.add("Python")
print(languages)  # Output: {'Python', 'C++', 'JavaScript', 'Java'} (order may vary)
# Remove "Java"
languages.remove("Java")
# Create another set of languages
web_languages = {"JavaScript", "HTML", "CSS"}
# Find common languages between the two sets
common_languages = languages.intersection(web_languages)
print(common_languages)  # Output: {'JavaScript'}

#Convert remove duplicates from a list using sets

array = [1, 2, 2, 3, 1, 4, 5, 3]  #declare list
nodupes = set(array)               #convert list into set. sets remove duplicates
unique_array = list(nodupes)      #creates new list using contents of set created from original list
unique_array = list(set(array))  #combines previous 2 steps into single step for
print(unique_array)