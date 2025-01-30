#python writing files (.txt, .csv, .xls, .xlsx)

text_data = "I like pizza!"

file_path = "output.txt"

try:
    with open(file_path, "a") as f:
        f.write("\n" + text_data)
        print("File created successfully!")

except FileExistsError:
    print("File already exists!")

# x mode: create a new file and open it for writing only if it does not exist

# w mode: open a file for writing only. If the file does not exist, create a new file. If the file exists, truncate it to zero length
# r mode: open a file for reading only. If the file does not exist, return an
# a mode: open a file for writing only. If the file does not exist, create a new file. If the file exists, append the data to the end of the file

Employees = ["eurico", "jose", "maria", "joao", "carlos"]

try:
    with open(file_path, "w") as f:
        for employee in Employees:
            f.write(employee + "\n")
        print("File created successfully!")

except FileExistsError:
    print("File already exists!")

