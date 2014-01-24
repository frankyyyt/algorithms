def is_prime(n):
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

primes = []
n = 2
while len(primes) <= 10000:
	if is_prime(n) == True:
		primes.append(n)
	n += 1
print primes
