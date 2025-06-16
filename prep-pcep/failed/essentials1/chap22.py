a_tuple = (1,2,5)

# tuples can appear on leftmost side of assigment operator

t1,t2,t3 = (0,0), (1,1), (2,2)
t4,t5,t6 = t1,t2,t3

phone_dict = {"Jennie": "111-222-3333", "Bob": "555-555-1234"}
print(phone_dict["Bob"])

dictionary = {"cat":"chat", "dog":"chien", "horse":"cheval", "ferret":"furet"}
words = ['cat', 'ferret', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")
#iterate through dictionary
for key in dictionary.keys():
    print(key, "->", dictionary[key])

for english, french in dictionary.items():
    print(english, "->", french)

dictionary['cat'] = 'minou'

for french in dictionary.values():
    print(french)

# add value
dictionary['swan'] = 'cygne'
#or
dictionary.update({"duck":"canard"})

#delete by key
del dictionary["horse"]
#delete last item
dictionary.popitem()
