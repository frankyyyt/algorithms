# A function that uses recursion to sum a list

def summer(L):
	print(L)
	if not L:
		return 0
	else:
		return L[0] + summer(L[1:])


summer([1,2,3,4,5])

# Recursively sum a tree

def treeSummer(L):
	total = 0
	for x in L:
		if not isinstance(x, list):
			total += x
		else:
			total += treeSummer(x)
	return total

print treeSummer([5, 3, [2, 3], 4, [[9, 2], 7]])

# Compare two binary trees?

