#calculates the sum of the digits of a given number.

def sum_of_digit(n): 
	
	sum = 0
	for digit in str(n): 
		sum += int(digit)	 
	return sum

n = 169
print(sum_of_digit(n))
