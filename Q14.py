#this program reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

def read_and_print_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    
    print("\nYou entered:")
    for line in lines:
        print(line)

# Run the function
read_and_print_lines()



