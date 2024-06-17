#program that converts a given string to uppercase.

def convert_to_uppercase(string):
  uppercase_string = ""
  for character in string:
    uppercase_string += character.upper()
  return uppercase_string


if __name__ == "__main__":
  string = "i love india"
  uppercase_string = convert_to_uppercase(string)
  print(uppercase_string)

  