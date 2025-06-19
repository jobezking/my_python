#tuples are like lists except immutable
numbers = (10, 5, 7, 2, 1)
print("Original: ", numbers)
print(len(numbers))
del numbers # deletes entire tuple
print(10 in numbers)
print(11 not in numbers)
new_numbers = numbers[1:3]
more_numbers = numbers[1:-1]
for number in numbers:
    print(numbers)