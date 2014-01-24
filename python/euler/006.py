numbers = range(1,101)

def sum_of_squares(numbers):
	return reduce(lambda x, y: x + y, [n ** 2 for n in numbers])

def square_of_sums(numbers):
	return reduce(lambda x, y: x + y, numbers) ** 2

print square_of_sums(numbers) - sum_of_squares(numbers)