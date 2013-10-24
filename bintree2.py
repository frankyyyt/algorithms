class Node():

	def __init__(self, value):
		self.left_child 	= None
		self.right_child 	= None
		self.parent 		= None
		self.value 			= value

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
	
root = Node("root")
root.insert_left_child("alibi")
root.insert_right_child("klipper")
root.right_child.insert_left_child("dudley")
root.right_child.insert_right_child("burp")
root.left_child.insert_left_child("thrud")
root.left_child.insert_right_child("muck")
root.left_child.left_child.insert_left_child("kreep")
root.left_child.left_child.left_child.insert_left_child("flinger")

node_count = 0
depth = 0
max_depth = 0

traverse(root)

print " "
print "Maximum depth of the tree is", max_depth
print "Number of nodes is:", node_count