#Variable scopes

def varfun():
    global x, y
    x = 3
    y = 2
    return x + y

varfun()