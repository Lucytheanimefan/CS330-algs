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

	def search(self, key, temp=None):
		if temp is None:
			temp = self.root
		if self.root.key is key:
			return 0
		elif key > temp.key:
			if key is temp.right.key:
				return str(temp.right)
			else:
				temp = temp.right
				self.search(key, temp)
		elif key < temp.key:
			print(str(key)+" < "+str(temp.key))
			if key is temp.left.key:
				print(str(key)+"=="+str(temp.left))
				print("EQUAL")
				print("Return this: "+str(temp.left))
				return str(temp.left)
			else:
				temp = temp.left
				print("New temp: "+str(temp))
				self.search(key, temp)
		else:
			return "not found"


if __name__ == "__main__":
	tree = BinaryTree()
	tree.insert(5)
	tree.insert(7)
	tree.insert(4)
	tree.insert(6)
	tree.insert(3)
	print(tree.search(3))







		
