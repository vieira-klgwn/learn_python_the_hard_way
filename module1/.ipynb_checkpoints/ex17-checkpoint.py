from sys import argv
from os.path import exists
#I wanna know if this creates these files automatically when you run the script. Perhaps, #know that tesxt.txt is not being created when i run the script, instead it is giving a #file not found error
from_file = "text.txt"
to_file = "new_text.txt"

print(f"Copying from \'{from_file}\' to \'{to_file}\'")

#we could do these two on one line , how?

in_file = open(from_file)
indata = in_file.read()


print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C  to abort.")
input()

out_file = open(to_file,'w')
out_file.write(indata)

print("Alright , all done.")

out_file.close()
in_file.close()
