#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
  """This function receives a CSV file as a parameter and returns a list of dictionaries from that file"""
  
  """The main purpose of this dialect is to remove any leading spaces while parsing the CSV file."""
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')

  employee_list = []
  for data in employee_file:
    employee_list.append(data)

  return employee_list


def process_data(employee_list):
  """process_data() should now receive the list of dictionaries, i.e., employee_list as a parameter and return a dictionary of department:amount"""

  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])

  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data


def write_report(dictionary, report_file):
  """This function writes a dictionary of department: amount to a file."""

  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()




employee_list = read_employees('/home/<username>/data/employees.csv')

dictionary = process_data(employee_list)

write_report(dictionary, '/home/<username>/data/report.txt')