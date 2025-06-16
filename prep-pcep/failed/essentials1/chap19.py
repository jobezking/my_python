def add3(a, b, c):
    return(c+a+b)

def add_and_mult_3(a, b, c):
    return c+a+b, c*a*b

add3(1,2,3)

d, e = add_and_mult_3(4,5,6)
print("a+b+c", d, "a*b*c", e)