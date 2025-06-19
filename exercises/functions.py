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