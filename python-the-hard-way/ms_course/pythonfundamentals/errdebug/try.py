numerator = 7
denominator = 0

def read_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")

read_file_contents("/Users/Example/Documents/my_file.txt")

try:
    result = numerator / denominator
    # this line might raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

try:
    file = open("data.txt", "r")
    # Process the file contents here
except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: You do not have permission to access this file.")

########

def get_city_population(populations, city):
    test = populations.get(city)
    if test is None:
            raise KeyError(f'City "{city}" not found in population data.')
    return test

city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}
city_name = "Tampa"

try:
    population = get_city_population(city_populations, city_name)
    print(f"The population of {city_name} is {population}")
except KeyError as error:
    print(error)

#Common Errors

# ZeroDivisionError
# FileNotFoundError
# TypeError: trying to perform an operation on incompatible types
# ValueError: trying to pass an inappropriate value to a function
# IndexError: trying to access a list or sequence element that is out of bounds
# ImportError: raised when an imported module or package cannot be found
# KeyError: raised when a dictionary key is not found
# AttributeError: raised when an attribute reference or attribute assignment fails
# SyntaxError: raised if there is a syntax error in code
# NameError: undefined variable
