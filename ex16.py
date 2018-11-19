from sys import argv
script, filename = argv
print(f"we're going ot erase {filename}.")
print("If you dont't want that , hit crtl-c (^C).")
print ("if you dont want that hit return")

input("?")

print ("opening the file......")
target = open(filename, 'w' )

print("truncating the file. goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 =input("line:")
line2= input("line2:")
line3 = input("line3:")

print("Im goin to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("And finally , we close it.")
target.close()
