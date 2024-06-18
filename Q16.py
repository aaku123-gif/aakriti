#program in python that counts the frequency of each character in a string.

def count_character_frequency(input_string):
    frequency = {}
    
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    return frequency

input_string = "i love india"
frequency = count_character_frequency(input_string)

print("Character frequency:")
for char, count in frequency.items():
    print(f"'{char}': {count}")

