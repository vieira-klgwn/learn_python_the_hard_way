from sys import argv

input_file = "ex20_test.txt"

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)
# Default open() mode is Readmode(r). When you open in Write mode("w" or "w+"), it #will truncate existing text in the file if that file exists. If that file does not #exits, it will create a new file with that name. 

#If you open it in append mode(a, or a+), the file pointer goes to the end of the file
# And there fore , when you try to read the file, it will read from the end of the 
# file, and hence you will see nothing until you take back the pointer to the 
# beginning of the file using seek(0) function.

print("First let's print the whole file: \n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
