import json

employee = {
    "name": "John Doe",
    "age": 30,
    "department": "Human Resources"
}

file_path = "output.json"

try:
    with open(file_path, "w") as f:
        json.dump(employee, f, indent=4)
        print("File created successfully!")

except FileExistsError:
    print("File already exists!")