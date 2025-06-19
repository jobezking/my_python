#Creating an instance of a class.
#When writing a Python class, you define a method called __init__ to be your constructor.
# prints "red"
class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"

honeycrisp = Apple()
print(honeycrisp.color)

#Modify variables
# prints "sweet" and "tart"
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")
print(honeycrisp.flavor)
print(fuji.flavor)

#special methods
# prints "an apple which is red and sweet"
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)

honeycrisp = Apple("red", "sweet")
print(honeycrisp)

jonagold = Apple("red", "sweet")
print(jonagold.color)
print(jonagold)