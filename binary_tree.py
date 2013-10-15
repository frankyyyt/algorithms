# traverse a binary tree

tree = [0, [1, [2, [3, 4]]]]


def traverse(tree):
	for branch in tree:
		if type(branch) == int:
			print branch, "stop"
		else:
			print "next"
			traverse(branch)

print tree
traverse(tree)

"""
		0
		|
	  1, 2
	  |




"""