def is_prime(n):
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

primes_sum = 0 
n = 2
while n <= 2000000:
	if is_prime(n) == True:
		primes_sum += n
	n += 1
print primes_sum
