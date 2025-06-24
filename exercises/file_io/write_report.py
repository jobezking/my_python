#!/usr/bin/env python3
import csv

#Convert employee data to dictionary
def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

#Process employee data
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

#Generate a report
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()


'''
Terms and definitions from course 2, module 2
Absolute path: A full path to the resource in the file system

Comma separated values (CSV): A very common data format used to store data as segment of text separated by commas

Dialects: Rules that define how a CSV file is structured

File systems: Methods and structures used to organize and control how data is stored and accessed

Mode: The format controlling what you can do with a recently opened file

Qwiklabs: An online learning environment or virtual machine to simulate real-world scenarios

Reader objects:  Object that represents an element or entity within a scene that needs to be rendered to the screen

Relative path: A portion of a path to show where the resource is located in relation to the current working directory

Virtual machine (VM): A computer simulated through software

Writer objects: The capability to write data to a CSV file
'''