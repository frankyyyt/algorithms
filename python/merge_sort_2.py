def merge(a, lo, mid, hi):
	i = lo
	j = mid+1

	# copy a into the aux array

	aux = a
	a = []

	# for every item in the array
	# either aux[lo:mid+1] half is empy
	# aux[mid+1:hi] half is empty
	# aux[lo:mid+1] < aux[mid+1:hi]
	# or aux[mid+1:hi] < aux[lo:mid+1]

	k = lo
	while k < hi:
		print aux[lo:mid+1], aux[mid+1:hi], i, j
		if aux[lo:mid+1] == []:
			a.append(aux.pop(j))
		elif aux[mid+1:hi] == []:
			a.append(aux.pop(i))
		elif aux[i] < aux[j]:
			a.append(aux.pop(i))
		else:
			a.append(aux.pop(j))
		print "A: ", a
		k += 1

	print a
	print "  "
	return a

a = ["E", "E", "G", "M", "R", "A", "C", "E", "R", "T"]
b = [3, 4, 5, 6, 1, 2, 3]
#merge(a, 0, 4, 10)
#merge(b, 0, 3, 6)

a = ['M', 'E', 'R', 'G', 'E', 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
a = ['C', 'B', 'A', 'D']

def sort(a, lo, hi):
	if hi - lo <= 1:
		return
	mid = lo + (hi - lo)/2
	print lo, mid, hi
	sort(a, lo, mid)
	sort(a, 1+mid, hi)
	merge(a, lo, mid, hi)

sort(a, 0, 3)


