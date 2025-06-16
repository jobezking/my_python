
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"Woof! My name is {self.name} and I'm a {self.breed}.")

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()