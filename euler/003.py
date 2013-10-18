print """

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def find_prime_factors(n):
	result = list()

	factor = n

	while factor > 1:
		print "checking factor", factor
		if n % factor == 0:
			print factor, "is a factor"
			if is_prime(factor) == True:
				result.append(factor)
		factor -= 1
	return result

def is_prime(n):
	if n % n == 0:
		x = n - 1
		while x > 1:
			print "testing if prime:", n, "%", x
			if n % x == 0:
				return False
			x -= 1
	return True

print find_prime_factors(600851475143)
