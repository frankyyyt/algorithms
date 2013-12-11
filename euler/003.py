def is_prime(n):
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def is_factor(number, i):
	if number % i == 0:
		return True
	return False

primes = []
n = 2
while len(primes) <= 10000:
	if is_prime(n) == True:
		primes.append(n)
	n += 1
print primes

'''
number = 600851475143
i = number
answer_found = False

while i > 1:
	if is_prime(i) == True:
		print i
	i -= 1

while i > 1 and answer_found == False:
	if is_factor(number, i) == True:
		print i, "is a factor"
		if is_prime(i) == True:
			print i
			answer_found = True
	i -= 1
'''
