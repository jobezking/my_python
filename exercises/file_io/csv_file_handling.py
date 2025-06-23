#Read data as CSV

import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()

# If the number of rows are unknown

import csv

with open('your_file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"Row: {row}, Number of columns: {len(row)}")

#Write data as CSV

import csv

hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]] #list of lists
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

#use dictionaries
#read
with open('software.csv', 'r') as software: 
    reader = csv.DictReader(software)
    for row in reader:
      print(("{} has {} users").format(row["name"], row["users"]))

#write
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

# Using pandas
import pandas as pd

# Assuming 'your_file.csv' might have varying column counts
df = pd.read_csv('your_file.csv')

# You can inspect the DataFrame's shape
print(df.shape) # (number_of_rows, number_of_columns_in_longest_row)

# Accessing data will show NaNs for missing values
print(df)

# https://docs.python.org/3/library/csv.html

# https://realpython.com/python-csv/