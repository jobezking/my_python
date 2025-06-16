def ex33fun(y,nums):
    print(f"At the top i is {y}")
    nums.append(y)

    y += 1
    print("Numbers now: ", nums)
    print(f"At the bottom of i is {y}")
    return(y,nums)

range = int(input("How many?: "))
i = 0
numbers = []

while i < range:
    i, numbers = ex33fun(i,numbers)


print("The numbers: ")

for num in numbers:
    print(num)