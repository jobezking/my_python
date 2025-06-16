def factorial_iterative(num): # factorial function iterative
    cur_val = 1

    for i in range(1, num + 1):
        cur_val *= i
        return cur_val
    
def factorial_cursive(num):
    if num != 1:
        return num * factorial_cursive(num -1)
    else:
        return num
    
#Lamda functions. Ideal for modules and class static methods
# A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

cube = lambda width, length, height : width * length * height   # How to define the lambda

box_volume = cube(4,5,6) # How to use the lambda

# zip()  combines multiple iterables such as lists, tuples, strings, dict etc, into a single iterator of tuples.
# zip() can be used to convert a dictionary into a list

ex_dict = {"key1": 31, "key2" : 29, "key3" : 45, "key4": 97, "key5": 72}
min_value = min(zip(ex_dict.values(), ex_dict.keys())) # find minimum dictionary value
max_value = max(zip(ex_dict.values(), ex_dict.keys())) # find maximum dictionary value
sorted_dict = sorted(zip(ex_dict.values(), ex_dict.keys())) # sorted dictionary

#topic: Multi-threading
## performance counter to run on single thread
from time import perf_counter, sleep

list_1 = ['microphone', 'cup', 'TV', 'wallet', 'hat']
start = perf_counter()

def print_function():
    sleep(1)
    for i in list_1:
        print("Value " + i)
        print()

print_function()
end = perf_counter()
print('Time to finish: {} seconds '.format(round(end-start, 2)))

#multi-threaded performance counter
#from time import perf_counter, sleep  already done earlier
import threading
list_1 = ['microphone', 'cup', 'TV', 'wallet', 'hat']
start = perf_counter()

def print_function2():
    sleep(1)
    for i in list_1:
        print("Value " + i)
        print()

t1 = threading.Thread(target=print_function2)  # create thread 1 which runs print_function2()
t2 = threading.Thread(target=print_function2)  # create thread 2 which runs print_function2()
t3 = threading.Thread(target=print_function2)  # create thread 3 which runs print_function2()
t4 = threading.Thread(target=print_function2)  # create thread 4 which runs print_function2()

t1.start() 
t2.start() 
t3.start() 
t4.start() 

t1.join() 
t2.join() 
t3.join()
t4.join()
end = perf_counter()
print('Time to finish: {} seconds '.format(round(end-start, 2)))

#JSON
import json
test_json = '{"Name": "Nneka", "Friends": ["Adeya", "Dola"]}'
dictionary_from_json = json.loads(test_json)
# read json file example
infile = open("file.json", "r")
json_file = json.load(infile)
print(json_file)
#typical method
path = '../test.json'
with open(path) as f:
    json_file = json.load(f)
    print(json_file)
#get crazy ... who cares about try-catch
print(json.load(open("file.json", "r")))

#json.dumps() turns dictionary into JSON
dx = {1: 'This', 2: 'Program', 3: 'Is', 4: 'Python', 5: 9, 'Python': 4}
dx_json = json.dumps(dx)

#store dictionary as json file with json.dump()
json.dump(dx, open('/mnt/data/dx.json',"w"))