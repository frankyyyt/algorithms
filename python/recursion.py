from test import testEqual
def removeWhite(s):
	if len(s) <= 1:
		return s
	else:
		return s[0].lstrip(" '") + removeWhite(s[1:].lstrip(" '"))

def isPal(s):
	if len(s) <= 1:
		return True
	elif len(s) == 2:
		if s[0] == s[-1]:
			return True
		else:
			return False
	else:
		if s[0] == s[-1]:
			return isPal(s[1:-1])
		else:
			return False

print isPal(removeWhite("x"))
print isPal(removeWhite("radar"))
print isPal(removeWhite("hello"))
print isPal(removeWhite(""))
print isPal(removeWhite("hannah"))
print isPal(removeWhite("madam i'm adam"))

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

