class Car:
 #The __init__ method: A special constructor. The __init__ method, often called the constructor, 
 # is a special method that Python automatically calls when you create a new object of your class. 
 # Its primary role is to initialize the object's attributes with appropriate values. 
 # This ensures that every new object starts with a valid state.   
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_level = 100  # Initial fuel level
    #    
    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine roars to life!")

    def accelerate(self):
        print(f"The {self.color} {self.make} {self.model} picks up speed!")

    def brake(self):
        print(f"The {self.make} {self.model} comes to a smooth stop.")
