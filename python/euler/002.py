print """
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

x = 1
y = 2
result = 2

print x
print y

while y <= 4000000:
	x = x + y
	if x % 2 == 0:
		print x, "is even"
		result += x
	else:
		print x, "is odd"
	y = y + x
	if y % 2 == 0:
		print y, "is even"
		result += y
	else:
		print y, "is odd"
print "result:", result