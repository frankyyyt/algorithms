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
	print node.value

	if node.parent != None:
		print "( parent is", node.parent.value, ")"

	if node.left_child == None and node.right_child == None:
		print "I reached the bottom!"

	if node.left_child != None:
		traverse(node.left_child)

	if node.right_child != None:
		traverse(node.right_child)
	

		
root = Node("root")
root.insert_left_child("alibi")
root.insert_right_child("klipper")
root.right_child.insert_left_child("dudley")
root.right_child.insert_right_child("burp")
root.left_child.insert_left_child("thrud")
root.left_child.insert_right_child("muck")
root.left_child.left_child.insert_left_child("kreep")

traverse(root)
