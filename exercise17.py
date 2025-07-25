# Exercise-17
print("Exercise 17: More Files", end="\n\n")
from genericpath import exists
from sys import argv
script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")
# We could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()
print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")
input()
out_file = open(to_file, 'w')
out_file.write(indata)
print("Alright, all done.")
out_file.close()
in_file.close()