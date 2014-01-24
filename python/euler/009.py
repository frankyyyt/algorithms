a = 0
b = 0
c = 0

def is_triplet(a, b, c):
	if (a*a) + (b*b) == (c*c):
		return True
	else:
		return False
c = 5
a = 1
b = c - 1

while a < 99:
	a += 1
	b -= 1
	if is_triplet(a, b, c) == True:
		print a, b, c
