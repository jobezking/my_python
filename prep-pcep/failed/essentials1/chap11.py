counter = 3
while counter != 0:
    print(counter)
    counter -= 1

#alternatively
counter = 3
while counter:
    print(counter)
    counter -= 1

i = 0 
while i < 100:
    print(i)
    i += 1
#alternatively
for i in range(100): 
    print(i)
#alternatively
for i in range(100): print(i)

for i in range(10,100): print(i)  # go from 10 to 100

for i in range(10, 100, 5): print(i)  # go from 10 to 100 in increments of 5

for i in range(100): 
    if i % 3:
        continue        # skip to next iteration of loop
    if i % 7:
        break           # end loop
    print(i)

#else is a rarely used feature in while and for loops
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else")

for i in range(100): 
    print(i)
else: 
    print("else")