#dictionary is variable = {key:value, key:value, ... key_n:value_n}
emtpy_dictionary = {}
language_dictionary = {"cat": "chat", "dog":"chien", "horse": "cheval", "ferret":"furet"}
phone_numbers = {'boss':123456789, 'elder':5554443333}
print(len(phone_numbers)) #returns the number of key-value pairs, which is 2

#iteration
for key in language_dictionary: #prints keys
    print(key)

for value in language_dictionary.values():
    print(value) #prints values

#use list or tuple
animal_keys = ('cat', 'dog', 'horse', 'tiger', 'ferret')
for animal in animal_keys:
    if animal in language_dictionary:
        print(animal, "->", language_dictionary[animal])
    else:
        print(animal, "is not in dictionary")

#dictionary methods and functions
for value in language_dictionary.values():
    print(value) #prints values

for key in language_dictionary.keys():
    print(key, "->", language_dictionary[key])

for eng, fr in language_dictionary.items(): #this the key the label eng and value the label fr
    print(eng,"->",fr)

for key in sorted(language_dictionary.keys()):  #sorts dictionary
    print(key, "->", language_dictionary[key])

#merge lists
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
#result: shirt will be same. jeans will only have white. scarf and socks will be added to list
#modify/add/remove
phone_numbers['boss'] = 4445551526 #modify
phone_numbers['church'] = 4442221111 #add
del phone_numbers['boss'] #delete
language_dictionary.popitem()   #deletes last item

def email_list(domains):
    emails = []
    for domain,users in domains.items():
        for user in users:
            emails.append(user + '@' + domain)
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group in group_dictionary:
        # Now go through the users in the group
        for user in group_dictionary[group]:
            # Now add the group to the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
