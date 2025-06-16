class Employee:         #to create a placeholder class just use declaration with pass statement
    pass

class Employee2:

    location = "Lagos, Nigeria"                      # class variable

    def __init__(self, name, email, role="janitor"): # defines class constructor with default role parameter
        self.name = name                             # assign first parameter
        self.email = email                           # assign second parameter
        self.role = role

    def getn(self):                                 # Normal methods that do not take parameters
        return self.name
    def getr(self):
        return self.role
    def gete(self):
        return self.email
    def getl(self):
        return self.location
    
    def setrole(cls, newrole):                      #class method that takes parameters. similar to init but uses cls instead of self
        cls.role = newrole

    @staticmethod
    def num_employees(employee_list):               # static method. Does not access class data or methods. used for factory methods.
        return len(employee_list)

emails = {'Joe Doe': 'jdoe@x.com', 'Jane Doe': 'doj@y.com', 'Sal Lee': 'sl@u.com', 'Tom Mix': 'tm@c.com'}

employees = []                              # create blank list for employee objets
for key in emails:                          # iterate through dictionary
    employee = Employee2(name=key, email=emails.get(key))  # key is name, use key in get() to access paired email address, create object
    if employee.email == 'sl@u.com':
        employee.setrole("civil engineer")
    employees.append(employee)              # add object to list 

for employee in employees:                  # iterate through resulting list
    print(f"N: {employee.getn()} E: {employee.gete()} R: {employee.getr()} L: {employee.getl()}")

print(f"{employees[0].num_employees(employees) } employees total") # never do this. just an example of class method