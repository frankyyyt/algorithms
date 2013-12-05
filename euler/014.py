def even_number(n):
	return n / 2

def odd_number(n):
	return (3 * n) + 1

def follow_chain(n):
	global length
	if n != 1:
		if n % 2 == 0:
			follow_chain(even_number(n))
		else:
			follow_chain(odd_number(n))
	length += 1

maximum = {"number": 0, "length": 0}

n = 1000000
while n >= 1:
	length = 0
	follow_chain(n)
	print "testing", n
	if length > maximum["length"]:
		maximum["length"] = length
		maximum['number'] = n

	n -= 1

print maximum