import csv

# Read a CSV file
with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
for row in csv_reader:
    print(row)