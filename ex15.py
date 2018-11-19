from sys import argv
## impirts the variable arugments from the sys module
script, filename = argv
#creates the variable filename to be read in
txt = open(filename)
#opens the file saned to the variable aruguments durin input
print (f"here's your file {filename}:")
print(txt.read())
## prints the out come 

print("type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())
