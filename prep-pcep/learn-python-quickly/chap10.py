# File Handling modes
# w = write only. will delete data if exists
# r = read only
# a = append only
# r+ = read and write
# rb = read binary      use binary for image and other non-text files
# wb = write binary
csv_file = open("customers-100.csv", "r") 
item1 = csv_file.readline() # reads a line and moves to next line in file
for eachline in csv_file:   #prints contents line by line
    print(eachline)
wholefile = csv_file.readlines() # reads entire file into list of strings. Optional parameter: max bytes to read


target_file = open("customers-100-copy.csv", "w")   # creates new file
target_file.write("There is one Lord, one faith, one baptism \n") #write to file. Newline character is needed to move to next line
csv_file.seek(0)    #seek() moves reference to position in file. Using 0 means going to beginning of file
for eachline in csv_file:   #copies old file to new line by line
    target_file.write(eachline) 

path = "/home/username/learnpy/prep-pcep/learn-python-quickly/testmod/customers-100.csv"
#For Windows: path = r"C:\Users\username\Desktop\customers-100.csv" Note that the 'r' keeps the path from being escaped
new_target = open(path, "r")
for i in new_target:
    print (i)

csv_file.seek(0)
get_ten_bytes = csv_file.read(10)   # reads 10 bytes from file
csv_file.close()
target_file.close()
new_target.close()

from os import remove, rename
rename("customers-100-copy.csv", "temp.txt")    #rename file
remove("temp.txt")                              # delete file