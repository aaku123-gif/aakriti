#program that checks if a substring is present in a given string

def check_substring(string, substring):
  if substring in string:
    return True
  else:
    return False

string = "Hello, how are you!"
substring = "India"

if check_substring(string, substring):
  print("Substring found!")
else:
  print("Substring not found.")

