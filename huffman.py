arr = ['a', 'b', 'c', 'd', 'e', 'f'];
freq = [5, 9, 12, 13, 16, 45];

class Node:
	def __init__(self, letter=None, freq=None):
		self.letter = letter
		self.freq = freq
		self.left = None
		self.right = None

	def __str__(self): 
		return letter + ": "+freq



class HuffmanTree:
	def __init__(self):
		self.root = Node(None, 0)

	def insert(head, letter, freq):
		if self.root is None or head is None:
			self.root = node
		elif head.right and freq > :


