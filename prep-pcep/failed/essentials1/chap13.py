# Lists
numbers = [0, 1, 2, 3, 4, 5]

position = numbers[-1] # position = 5
position = numbers[-2] # position = 4

numbers_length = len(numbers)

del numbers[1]

numbers.append(6) # adds to end
numbers.insert(7, 1) # adds to index 7

my_list = []

for i in range(5): my_list.append(i**i)
for i in range(len(my_list)): total += my_list[i]
#alternatively
for i in my_list: total += my_list[i]