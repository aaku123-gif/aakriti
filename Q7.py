#program that takes a string as input and return its length

def find_lenght(string):
    length=0
    for char in string:
        length+=1
    return length

string="how are you"
length=find_lenght(string)
print(length)