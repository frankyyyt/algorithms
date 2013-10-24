class Node():

	def __init__(self, value):
		self.left_child = None
		self.right_child = None
		self.parent = None
		self.value = value

	def insert_left_child(self, new_node):
		if self.left_child == None:
			self.left_child = Node(new_node)
			self.left_child.parent = self

	def insert_right_child(self, new_node):
		if self.right_child == None:
			self.right_child = Node(new_node)
			self.right_child.parent = self

def traverse(node):
	global node_count, max_depth, depth

	node_count += 1
	depth += 1

	print node.value

	if node.parent != None:
		print "	( parent is", node.parent.value, ")"

	if node.left_child == None and node.right_child == None:
		print "	I reached the bottom at depth", depth
		if depth > max_depth:
			max_depth = depth

	if node.left_child != None:
		traverse(node.left_child)
		depth -= 1

	if node.right_child != None:
		traverse(node.right_child)
		depth -= 1

def compare_trees(node1, node2):
	if node1 and node2:
		print node1.value, node2.value, node1.value == node2.value
	else:
		print "Node missing on one side", False
		return

	if node1.left_child != None or node2.right_child != None:
		compare_trees(node1.left_child, node2.right_child)

	if node1.right_child != None or node2.left_child != None:
		compare_trees(node1.right_child, node2.left_child)

root = Node("root")
root.insert_left_child("alibi")
root.insert_right_child("klipper")
root.right_child.insert_left_child("dudley")
root.right_child.insert_right_child("burp")
root.left_child.insert_left_child("thrud")
root.left_child.insert_right_child("muck")
root.left_child.left_child.insert_left_child("kreep")
root.left_child.left_child.left_child.insert_left_child("flinger")
#root.left_child.left_child.left_child.left_child.insert_left_child("flingerjr")

root2 = Node("root")
root2.insert_right_child("alibi")
root2.insert_left_child("klipper")
root2.left_child.insert_right_child("dudley")
root2.left_child.insert_left_child("burp")
root2.right_child.insert_right_child("thrud")
root2.right_child.insert_left_child("muck")
root2.right_child.right_child.insert_right_child("kreep")
root2.right_child.right_child.right_child.insert_right_child("flinger")
root2.right_child.right_child.right_child.right_child.insert_right_child("flingerjr")

node_count = 0
depth = 0
max_depth = 0

print "Traversing from root"
traverse(root)

print " "
print "Maximum depth of the tree is...", max_depth
print "Number of nodes is:", node_count

node_count = 0
depth = 0
max_depth = 0

print ""
print ""
print "Traversing from root2..."
traverse(root2)

print ""
print "Maximum depth of the tree is", max_depth
print "Number of nodes is:", node_count
print ""
print ""
print "Checking if root and root2 are mirrors..."
compare_trees(root, root2)

