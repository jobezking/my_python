my_list = [0, 1, 2, 3, 4]
my_list2 = my_list[2:]      # when slicing, the second operand needs to be blank to pick up the last index
print (my_list2)

del my_list[0:2]  # del can also delete slices

my_list = [0, 1, 2, 3, 4]
print(5 in my_list)      # "in" returns true if value is in list
print(4 not in my_list)  # "not in" returns true if value is not in list