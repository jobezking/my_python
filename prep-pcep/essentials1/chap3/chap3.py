var = 0
print(var == 0) # True
var = 1
print(var == 1) # True
numbers = [1, 2, 3, 4, 5]
ints = [10, 5, 7, 2, 1]
floats = [10., 5., 7., 2., 1.]
characs = ['a','b', 'c', 'd', 'e'] 
a_list = [numbers, ints, floats, characs]
print(a_list)
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(numbers[-4])
print(numbers[-5])
print(numbers[-len(numbers)])
print(numbers[-len(numbers) + 1])
numbers.append(3)
numbers.insert(-2, 4)
for j in numbers:
    print(j)
for j in range(len(numbers)):
    print(j)

#bubble sort
#method 1 ... does not work!
my_list = [8, 10, 6, 2, 4]
for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

my_list = [8, 10, 6, 2, 4]
swapped = True

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

my_list = [8, 10, 6, 2, 4]
my_list.sort()
my_list.reverse()

list1 = [1]
list2 = list1
list1[0] = 2
print(list2)  # will output 2 as list2 and list1 refer to the same pointer
mylist = my_list[:] # copies my_list
print(mylist)
print(my_list * 3)