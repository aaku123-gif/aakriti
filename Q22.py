#this program returns the minimum and maximum values in a list of numbers.

def find_min_max(numbers):
    if not numbers:
        return None, None 
    
    min_val = float('inf')
    max_val = float('-inf')  
    
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return min_val, max_val

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 4, 7, 5]
min_val, max_val = find_min_max(numbers)
print(f"List: {numbers}")
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")

