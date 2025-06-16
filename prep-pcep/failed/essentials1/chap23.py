try:
    value = int(input('Enter a natural number: '))
    print("The reciprocal of", value is 1/value)
except ValueError:
    print("I do not know what to do")
except ZeroDivisionError:
    print('Division by zero is not allowed')
except: # default exception
    print("Generic Error")

'''
ZeroDivisionError
ValueError: when a function like int() or float() receives a properly typed argument with an unacceptable value
TypeError: when you attempt to apply data whose type is unacceptable i.e. float to int
AttributeError: when you try to activate a method that doesn't exist in an item you are dealing with (?)
SyntaxError
'''