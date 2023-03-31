# Python program to demonstrate
# seek() method

f = open("GfG.txt", "r")
# Second parameter is by default 0
# sets Reference point to twentieth
# index position from the beginning
f.seek(20)

#Tell method
# prints current position
print(f.tell())
print(f.readline())
f.close()

#Truncate method
# The truncate() method resizes the file to the given number of bytes.
# If the size is not specified, the current position will be used.
# Syntax
# file.truncate(size)