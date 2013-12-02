import random
def is_number_prime(n):
	# Fermat's little thorem
	a = random.randrange(2, n)
	b = a ** (n-1)

	if b % n == 1:
		return True
	else:
		return False

print is_number_prime(6)


prime_count = 1
current_prime = 3

n = 3

while prime_count <= 10001:
	if is_number_prime(n) == True :
		prime_count += 1
		current_prime = n
		#if prime_count % 100 == 0:
		print "prime #" + str(prime_count), "is", current_prime
	n += 1

