
# This Python program takes a string input from the user and writes it to a text file.

n = input("Enter a string: ")

with open("my_file.txt", "w") as f:
    f.write(n)

f.close()

print("The string has been written to the file.")

