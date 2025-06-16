### Chapter 2 Notes
function: cause some effect, evaluate a value, return it as the function's results. Name should be significannt. Can come from:
1. Python itself and its environment (built-in)
2. From modules (some come with Python, some require separate installation, some user-created)
3. write them yourself to make programs simpler, clearer, more elegant
Python functions can accept any number of arguments (including 0). Function arguments are not code but data.
When Python sees function invocation:
1. checks to see if function name is legal i.e. if a function with its name exists
2. checks if it has the required # of arguments
3. leaves program to jump into invoked function, passing any arguments
4. function executes its code
5. Python returns to your code to the place just after invocation and resumes execution, returning any results
print()
1. Takes arguments (any number of arguments including 0)
2. converts them into human-readable form if needed (strings don't need this)
3. sends resulting data to output device (usually console)
4. can accept virtually any types of arguments: strings, numbers, characters, logical values, objects
5. for our purposes, returns no values
6. automatically puts a space between outputted arguments i.e. in a comma-separated list
In Python there cannot be more than 1 instruction in a line
\n = newline  \ = escape character
positional function arguments: meaning of the argument is dictated by its position
end: print keyword argument to determine character sent at end of line i.e. end="\n"
sep: print keyword argument to determine separation character i.e. sep="-"
Literal: data whose value is determined by the literal itself. Meaning that it is not a variable
1. string
2. numbers (integers, floats, octal, hexadecimal). Type: characteristic of numeric value that determines kind, range and application
In Python, integers can be positive and negative and so can floats
Floats are declared by either decimal or letter e (for exponent). Otherwise Python will presume integer. 
Python will always choose the most economical form of a number's presentation.
3. boolean
Mathematical operations:
1. +: addition
2. -: subtraction
3. /: division
4. //: floor division (no remainder, lacks fractional component)
5. %: modulus (only remainder)
6. **: exponent
Due to left bindings, most Python mathematical expressions evaluate left to right. Difference?
9 % 6 % 2 when left to right is 1 ( 9 % 6 is 3, 3 % 2 is 1)
9 % 6 % 2 when right to left is divide by zero error ( 6 % 2 is 0, 9 % 0 is undefined)
Exception: exponents have righ-sided bindings

Priorities:
1. ~, +, - unary
2. **
3. *, /, //, %
4. +, - binary
5. << >> binary shift
6. <, <=, >, =>
7. ==, !=
8. &
9. |
10. =, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=

Bitwise operators:
& (conjunction, AND)
| (disjunction, OR)
~ (negation, NOT)
^ (exclusive or)
When multiple operators have the same priority, rely on binding order
Parenthesis can change order as values in parenthesis are calculated first
