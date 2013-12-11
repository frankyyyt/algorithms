def find_factorial_digits(n):
	digits = []
	factor = n
	while factor >= 1:
		digits.append(factor)
		factor -= 1
	factorial_digits = reduce(lambda x, y: x*y, digits)
	return factorial_digits

def sum_digits(n):
	digit_list = [int(x) for x in str(n)]
	digit_sum = reduce(lambda x, y: x + y, digit_list)
	return digit_sum

factorial_digits = find_factorial_digits(100)
print sum_digits(factorial_digits)
