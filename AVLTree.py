class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key
		self.height = 1

	def __str__(self):
		return "%s" %self.key

class AVLTree():
	def __init__(self, key):
		self.root = None
		self.height = -1
		self.balance = 0

	def rebalance(self):
		

	def insert(self, key):
		n = Node(key)

		if self.root is None:
			self.root = n
			n.left = AVLTree()
			n.right = AVLTree()
		elif key<self.root.key:
			self.root.left.insert(key) #recursive
		elif key>self.root.key:
			self.root.right.insert(key)

		self.rebalance()
