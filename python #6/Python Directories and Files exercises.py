#task 1
import os

def list_contents(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_contents = os.listdir(path)
    
    return directories, files, all_contents

specified_path = open(r"C:\Users\alizh\OneDrive\Рабочий стол\Works\4semestr\PP2\works\python lab 6")
directories, files, all_contents = list_contents(specified_path)
print("Directories:", directories)
print("Files:", files)
print("All Contents:", all_contents)

#task 2
import os

def check_path_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    
    return exists, readable, writable, executable

specified_path = open(r"C:\Users\alizh\OneDrive\Рабочий стол\Works\4semestr\PP2\works\python lab 6")
access_info = check_path_access(specified_path)
print("Existence:", access_info[0])
print("Readability:", access_info[1])
print("Writability:", access_info[2])
print("Executability:", access_info[3])

#task 3
import os

def path_info(path):
    exists = os.path.exists(path)
    if exists:
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return exists, filename, directory
    else:
        return exists, None, None


given_path = open(r"C:\Users\alizh\OneDrive\Рабочий стол\Works\4semestr\PP2\works\python lab 6")
path_exists, filename, directory = path_info(given_path)
if path_exists:
    print(f"Path exists. Filename: {filename}, Directory: {directory}")
else:
    print("Path does not exist.")


#task 4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)


text_file_path = open(r"C:\Users\alizh\OneDrive\Рабочий стол\Works\4semestr\PP2\works\python lab 6\a.txt")
line_count = count_lines(text_file_path)
print(f"Number of lines in the file: {line_count}")

#task 5
def write_list_to_file(file_path, content_list):
    with open(file_path, 'w') as file:
        for item in content_list:
            file.write(str(item) + '\n')

list_to_write = [1, 2, 3, 4, 5]
output_file_path = open(r"C:\Users\alizh\OneDrive\Рабочий стол\Works\4semestr\PP2\works\python lab 6\a.txt")
write_list_to_file(output_file_path, list_to_write)

#task 6
import string

def generate_files():
    for letter in string.ascii_uppercase:
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            pass  

generate_files()

#task 7
def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source_file, open(destination_path, 'w') as destination_file:
        destination_file.write(source_file.read())

source_file_path = open(r"C:\Users\alizh\OneDrive\Рабочий стол\Works\4semestr\PP2\works\python lab 6\a.txt")
destination_file_path = open(r"C:\Users\alizh\OneDrive\Рабочий стол\Works\4semestr\PP2\works\python lab 6\b.txt")
copy_file(source_file_path, destination_file_path)

#task 8
import os

def delete_file(file_path):
    exists = os.path.exists(file_path)
    if exists:
        os.remove(file_path)
        print(f"File at {file_path} deleted successfully.")
    else:
        print(f"File at {file_path} does not exist.")


file_to_delete = open(r"C:\Users\alizh\OneDrive\Рабочий стол\Works\4semestr\PP2\works\python lab 6\c.txt")
delete_file(file_to_delete)






