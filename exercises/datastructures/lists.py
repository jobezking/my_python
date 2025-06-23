numbers = [10, 5, 7, 2, 1]
print("Original: ", numbers)
numbers[0] = 111
print("New: ", numbers)
del numbers[3]
print(len(numbers))
numbers.append(7) #value to end of list
numbers.insert(3,5) #location, value
numbers.insert(-1,-1) #location, value
print(numbers)
del numbers[2] # deletes item from list
del numbers # deletes entire list
numbers.remove(7) #removes the first instance of 7

new_list = []

for i in range(5):
    new_list.append(i**i)
    print(i)

#comprehension means rewriting above as:
newer_list = [g ** g for g in range(5)]
print(new_list, newer_list)

a = 3
b = 4
a,b = b,a
print(f"a={a}, b={b}")
my_list = [10, 1, 8, 3, 5]
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

singers = []
for s in range(5):          #prompts the user for 5 singers
    singers.append(input())    #places 5 singers in the list
print(singers)

## add to beginning of list
a_list = []
for x in range(6):
    a_list.insert(0,x)
print(a_list)

#only print half of list
juke = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] #7 items. can't divide by 2 because it will leave a remainder
num = len(juke) // 2 # floor division will remove the remainder. Note that modulo % gives the remainder
for v in range(num):
    print(juke)         #will only print 'a', 'b', 'c'
#iterating through list
ages = [10, 30, 5, 90, 25]
for age in ages:
    print("User's age is: ", age)

#slicing
order = [0, 1, 2, 3, 4, 5]
new_order = order[1:3]
an_order = order[1:-1]
print(f"new_order{new_order}, an_order{an_order}")
#bubble sort
sort_list = [8, 10, 6, 4, 1, 4, 16, 88]
swapped = True
while swapped:
    swapped = False
    for i in range(len(sort_list) - 1):
        if sort_list[i] > sort_list[i+1]:
            swapped = True
            sort_list[i],sort_list[i+1] = sort_list[i+1], sort_list[i]

if 8 in sort_list:
    print("True")
if 50 not in sort_list:
    print("False")