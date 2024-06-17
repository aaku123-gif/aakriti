# program that reads the content of a text file and prints it to the console.

def read_file(filename):
  with open(filename, "r") as f:
    content = f.read()
  return content

def print_to_console(content):
  print(content)

if __name__== "__main__":
  filename = "my_file.txt"
  content = read_file(filename)
  print_to_console(content)
  



