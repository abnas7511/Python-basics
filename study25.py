import csv

employees = [["Name", "Age", "Job"],
             ["John Mckee", 38, "Sales"],
             ["Lisa Crawford", 29, "Marketing"],
             ["Sujan Patel", 33, "HR"]]

file_path = "employees.csv"

try:
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(employees)
        print(f"csv file created: {file_path}")
except FileExistsError:
    print(f"csv file already exists: {file_path}")

#read from files


file_path1 = "output.txt"

try:
    with open(file_path1, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"file not found: {file_path1}")

#reading from a json file

import json

file_path2 = "output.json"

try:
    with open(file_path2, "r") as f:
        content = json.load(f)
        print(content)
except FileNotFoundError:
    print(f"file not found: {file_path2}")

#reading from a csv file


file_path3 = "employees.csv"
try:
    with open(file_path3, "r") as f:
        content = csv.reader(f)
        for line in content:
            print(line)

except FileNotFoundError:
    print(f"file not found: {file_path3}")