'''
Study guide: Files and directories
Managing files and directories includes creating, deleting, and moving files and directories. It also includes changing ownership and permissions of the files and directories. 
There are several ways to manage files and directories in Python. One of the easiest ways is to use low-level functions in the OS and SYS modules that closely mimic standard 
Linux commands such as os.mkdir()and  os.rmdir(). Alternatively, you can utilize the Pathlib module, which provides an object-oriented interface to working with the file systems. 

Let’s take a look at two examples. The first example uses OS; the second uses Pathlib. These two code examples do the same thing: 
They create a directory called test1 and move a file named README.md from the sample_data folder into test1.

An example of using the OS function to create a directory and move a file:
'''

# Create a directory and move a file from one directory to another
# using low-level OS functions.

import os

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
  os.mkdir(dest_dir)

# Construct source and destination paths:
src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
dest_file = os.path.join(os.getcwd(), "test1", "README.md")

# Move the file from its original location to the destination:
os.rename(src_file, dest_file)

# Create a directory and move a file from one directory to another
# using Pathlib.

from pathlib import Path

# Check to see if the "test1" subdirectory exists. If not, create it:
dest_dir = Path("./test1/")
if not dest_dir.exists():
  dest_dir.mkdir()

# Construct source and destination paths:
src_file = Path("./sample_data/README.md")
dest_file = dest_dir / "README.md"

# Move the file from its original location to the destination:
src_file.rename(dest_file)

'''
The OS module 
Python’s OS module, or the miscellaneous operating system interface, is very useful for file operations, directories, and permissions. Let’s take a look at each.

File operations
File names can be thought of as two names separated by a dot. For example, helloworld.txt is the file name and the extension defines the file type. OS provides functions to create, read, update, 
and delete files. Some of the basic functions include:

Opening and closing files

Reading from and writing to files

Appending to files

Directories
OS also provides functions to create, read, update, and delete directories, as well as change directories and list files. Knowing how to use these functions is key to working with files.
For example, os.listdir( path ) returns a list of all files and subdirectories in a directory.

Permissions
Having the ability to update file permissions is an important aspect of making installations from a terminal window. The os.chmod() provides the ability to create, read, and update permissions for individuals or groups.

Things to keep in mind  
One thing to be aware of is that Python treats text and binary files differently. Because Python is cross-platform, it tries to automatically handle different ASCII line endings. 
If you’re processing a binary file, make sure to open it in binary mode so Python doesn’t try to “fix” newlines in a binary file.

A best practice is to always close() a file when you’re done reading or writing to it. Even though Python usually closes them for you, it’s a good signal to other people reading 
your code that you’re done with that file. Make sure to catch any potential errors from filesystem calls, such as permission denied, file not found, and so on. Generally, 
you wrap them in try/except to handle those errors.

Key takeaways
There are several ways to manage files and directories in Python. One way is to use low-level functions in the OS and SYS modules that closely mimic standard Linux commands. 
Another way is to utilize the Pathlib module, which provides an object-oriented interface to working with the file systems. 

Resources for more information
More information about files and directories can be found in several resources provided below: 

https://docs.python.org/3/library/os.html
https://docs.python.org/3/library/os.path.html
https://en.wikipedia.org/wiki/Unix_time
'''
