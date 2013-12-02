numbers = range(1, 21)

i = 1

def test_all_numbers(i):

	for number in numbers:
		if i % number != 0:
			return False
	return True

while i <= 300000000:
	if test_all_numbers(i) == True:
		print i
	i += 1
