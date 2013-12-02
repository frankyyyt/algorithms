two_digit_numbers = range(100, 1000)

palindromes = list()

for first_number in two_digit_numbers:
	for second_number in two_digit_numbers:
		result = first_number * second_number
		if str(result) == str(result)[::-1]:
			palindromes.append(result)

palindromes.sort()
print palindromes