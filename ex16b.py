from sys import argv
script, filename = argv
file =open(filename)

print(f"we are going to read the text in {file}")

print(file.read())
