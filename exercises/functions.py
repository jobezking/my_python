#break string up into words function
def breakup_char(sentence):
    for character in sentence:
        print(character)

def breakup_words(sentence):
    words = sentence.split()
    for word in words:
        print(word)

def show_string_indexes(sentence):
    for a, char in enumerate(sentence):
        print(f"Index {a}: {char}")

tester = "This is a short sentence"
breakup_char(tester)
breakup_words(tester)
show_string_indexes(tester)

#factorial

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range (2, n + 1):
        product = product * i

    return product

print( factorial_function(10))

#recursion
def fibonacci(q):
    if q < 1:
        return None
    if q < 3:
        return 1
    return fibonacci(q - 1) + fibonacci(q - 2)

print(fibonacci(7))