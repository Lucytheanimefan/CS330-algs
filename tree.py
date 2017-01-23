class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key
		self.height = 1

	def __str__(self):
		return "%s" %self.key

class BinaryTree():
	def __init__(self):
		self.root = None
		self.height = 0
		self.balance = 0

	def insert(self, key, temp=None):
		if temp is None:
			temp = self.root
		if self.root is None:
			#set the root as the node
			self.root = Node(key)
		elif key > temp.key:
			if temp.right is None:
				temp.right = Node(key)
			else:
				temp = temp.right
				self.insert(key, temp)
		elif key < temp.key:
			if temp.left is None:
				temp.left = Node(key)
			else:
				temp = temp.left
				self.insert(key, temp)


if __name__ == "__main__":
	tree = BinaryTree()
	tree.insert(5)
	tree.insert(7)
	tree.insert(4)
	tree.insert(6)
	tree.insert(3)
	print(tree.root)
	print(tree.root.right)
	print(tree.root.left)
	print(tree.root.right.left)
	print(tree.root.left.left)







		
