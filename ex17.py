from sys import argv
#allows me to take command line arguments 
from os.path import exists
#imports modules that allow me to read and write files
script, from_file, to_file = argv

print(f"copying from {from_file}to {to_file}")
in_file =open(from_file)
in_data =in_file.read()

print(f"the input file is {len(in_data)}")
print(f"does tthe ouput file eist? {exists(to_file)}")
print("ready , hit return to coninure, ctrl-c to abort")
input()

out_file =open(to_file ,'w')
out_file.write(in_data)
out_file.close()
in_file.close()
