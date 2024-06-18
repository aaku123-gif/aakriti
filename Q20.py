#this program takes a list of numbers and returns their sum.

def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers_list = [1, 2, 3, 4, 5 ,6 ]
result = calculate_sum(numbers_list)
print(f"The sum of the numbers {numbers_list} is: {result}")
