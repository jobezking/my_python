#Inheritance, child classes, special methods

class Employee:                             #main class
    location = "Accra, Ghana"
    def __init__(self, name, email, role):
        self.name = name
        self.role = role
        self.email = email
    def get_info(self):
        return '{} {} {}'.format(self.name, self.email, self.role)
    
class Developer(Employee):             #child class inherited from Employee
    def __init__(self,name,email,role,language):
        super().__init__(name,email,role)       # super accesses parent class
        self.language = language
    def get_info(self):
        return super.get_info() + ' {}'.format(self.language)
'''
Multiple inheritance: inherit from multiple classes. 
Specify parent classes in the class creation statement and specify the attributes to be inherited when initializing child class.
By default the child chlass whill have access to methods of both parent classes.
'''
class Equipment:                             #new class
    def __init__(self,type,owner):
        self.type = type
        self.owner = owner
    def show_equipment(self):
        return '{} - owned by: {}'.format(self.type, self.owner)

class Developer2(Employee, Equipment):
    def __init__(self,name,email,role,language,type, owner):
        super().__init__(name,email,role)
        self.type = type
        self.owner = owner
        self.language = language
    def get_info(self):
        return '{} {} {}'.format(self.name, self.email, self.role)

    
manager = Employee('Bob Lee', 'blee@u.net', 'manager')
devmanager = Developer('Joe Ham', 'jham@z.com', 'manager', 'Golang')
altdev = Developer(manager.name, manager.email, manager.role, "R" )
print(manager.email)
print(devmanager.email, devmanager.language)
print(altdev.language)

equip1 = Equipment("Macbook", "Company")
equip2 = Equipment("Ubuntu Desktop", "Personal")

emp1 = Developer2("Ray Hope", "rhope@t.com", "software engineer", equip1.type, equip1.owner, "Java")
emp2 = Developer("John Ton", "jton@q.org", "web architect", equip2.type, equip2.owner, "Typescript")
print(emp1.show_equipment()) 
print(emp2.show_equipment())

#import class from file (can also import entire file with import class2import)

from class2import import MyClass

# Create an instance of MyClass
student = MyClass("Adebayo")

# Call a method of MyClass
print(student.greet())  # Output: Hello, my name is Adebayo

'''
isinstance() and issubclass() to check if objects are instances of subclasses. 
isinstance() takes an object and the class in question as arguments 
issubclass() takes the names of two classes, checking to see if the first class is a subclass of the second.
'''
print(isinstance(manager, Employee))        # is object manager an instance of class Employee
print(issubclass(Developer, Employee))      # is class Developer a subclass of Employee