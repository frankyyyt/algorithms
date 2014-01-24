A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def merge_sort(A, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	L = [None for x in range(1, n1 + 1)]
	R = [None for x in range(1, n2 + 1)]
	for i in range(0, n1):
		L[i] = A[p + i - 1]
	for j in range(0, n2):
		R[j] = A[q + j]
	L.append("s")
	R.append("s")
	i = 0
	j = 0
	for k in range(p-1, r):
		print "comparing", L[i], "and", R[j]
		if L[i] <= R[j]:
			print L[i], "is less than", R[j]
			A[k] = L[i]
			i = i + 1
		else: 
			print "setting", k, "in A to", R[j]
			A[k] = R[j]
			j = j + 1
	return L, R, A

print merge_sort(A, 1, 5, 10)
