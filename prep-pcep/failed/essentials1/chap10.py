'''
operator priority
+, - (unary)
**
*, /, %, *
+, - (binary i.e. for arithmetic)
<, <=, >, >=
==, !=
'''

x = 3
if x >= 5:
    print(x)
elif x < 3:
    print(x**2)
elif x > 1:
    print(x+x)
else:
    print("Invalid")

#this is valid. Should any if-elif-else branch contain only one instruction, the conditional and the instruction can share the same line
y = 9
if y < 3: print("Too big")
else: print("Too small")