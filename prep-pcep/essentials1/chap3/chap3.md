### Chapter 3 Notes
The equality, ==, operator has a low priority. Thus:
black_sheep = 2 * white_sheep
is the same as
black_sheep = (2 * white_sheep)
Conditional Statement must contain in this order:
1. if keyword
2. one or more whitespaces
3. an expression (question or answer) whose value will be solely interpreted as true for false
4. a colon followed by a newline
5. indented instruction or set of instructions, either 4 spaces of indentation or a tab (cannot mix spaces and tabs for indentation)
Infinite loop example!
while True:
    print("I am stuck inside a loop.")

while number: is the same as while number != 0:
if number % 2 == 1: is the same as if number %2:
break: exits the loop immediately
continue: goes back to start of loop i.e. while i < 2: immediately (in while loops can be used to skip counter)

While loops can have else branch. It will always be executed once even if the loop is never entered (effectively a do loop)
i = 10
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

For loops operate the same, except if the loop counter is initialized in the for statement, it will be out of scope for the else loop i.e.:
for i in range(5):
    print(i)
else:
    print("else", i)     #will give NameError: name 'i' is not defined
