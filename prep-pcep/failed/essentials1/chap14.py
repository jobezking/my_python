# bubble sort a list

my_list = [8, 10, 6, 2, 4]
is_swap = True

while is_swap:
    is_swap = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[ i + 1]:
            is_swap = True
            my_list[i], my_list[i + 1 ] = my_list[i+1], my_list[i]