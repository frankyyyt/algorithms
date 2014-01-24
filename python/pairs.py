a = [1, 2, 3]
b = [4, 5, 6]

# what are all the possible pairs in a and b?

for i in a:
	for j in b:
		print i, j


for i in b:
	for j in a:
		print i, j
