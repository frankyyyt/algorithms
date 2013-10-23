class Node():

	def __init__(self, value):
		self.left_child = None
		self.right_child = None
		self.value = value

	def get_left_child(self):
		return self.left_child

	def get_right_child(self):
		return self.right_child

	def get_value(self):
		return self.value

	def insert_left_child(self, new_node):
		if self.left_child == None:
			self.left_child = Node(new_node)

	def insert_right_child(self, new_node):
		if self.right_child == None:
			self.right_child = Node(new_node)

def traverse(node):
	print node.value
	if node.left_child != None:
		traverse(node.left_child)
	#else: 
		# go up one level and check right child

root = Node("root")
root.insert_left_child("alibi")
root.left_child.insert_left_child("thrud")
root.left_child.insert_right_child("muck")
root.left_child.left_child.insert_left_child("kreep")
#print root.left_child.left_child.left_child

node = root
traverse(node)
