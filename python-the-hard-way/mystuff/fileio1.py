#"x" - Create - will create a file, returns an error if the file exists
#"a" - Append - will create a file if the specified file does not exists
#"w" - Write - will create a file if the specified file does not exists
# https://www.geeksforgeeks.org/open-a-file-in-python/

test_file = "alfresco.log"
debug_file = "debug.log"

try:
    with open(test_file, 'r') as file:
        # Read the lines of the file
        pass

except FileNotFoundError:
    print(f"File '{test_file}' not found")
except PermissionError:
    print("You don't have permission to access this file.")    
except Exception as e:
    print(f"An error occurred: {e}")

file = open(test_file, 'r')
test_file_processed = open(debug_file, 'a')
#reads and prints entire file. Just done for testing but doesn't suit our purposes
#file_content = file.read()
#print("File Content:\n", file_content)
debug_s="DEBUG"
line = file.readline()
while line:
    if (line.find(debug_s) != -1):
        test_file_processed.write(line)
    line = file.readline()

test_file_processed.close()
test_file_processed = open(debug_file, 'r')
test_file_processed_output = test_file_processed.read()
print("File Content:\n", test_file_processed_output)
file.close()
test_file_processed.close()