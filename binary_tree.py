# traverse a binary tree

tree = [0, [1, 2], [3, [4, 5]]]


def traverse(tree):
	for branch in tree:
		if type(branch) == int:
			print branch
		else:
			traverse(branch)

traverse(tree)