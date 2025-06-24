'''
The mode argument is optional, and it specifies the mode in which the file is opened. If omitted, it defaults to ”r” and that means opening for reading in text mode. The common modes include:
"r"  open for reading (default)
"w"  open for writing, truncating the file first
"x"  open for exclusive creation, failing if the file already exists
"a"  open for writing, appending to the end of the file if it exists
"+"  open for both reading and writing
Attempting to write to a file opened for read (“r”) will cause a runtime error.
'''

with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

with open("sample_data/declaration.txt", "rt") as textfile:
    for line in textfile:
        print(line)

f = open("sample_data/declaration.txt", "w")

f = open('workfile', 'w', encoding="utf-8") 
