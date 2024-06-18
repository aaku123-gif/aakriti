#this program removes all punctuation from a given string

import string

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

input_string = "Hello, guys! this is python."
output_string = remove_punctuation(input_string)
print(output_string)
