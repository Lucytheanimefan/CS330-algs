
class Node:
	def __init__(self, value=None, weight = None, nextNode=None):
		self.value = value
		self.weight = weight
		self.next = nextNode

	def __str__(self): 
		return "Value: "+str(self.value)+", weight: "+str(self.weight)


class Graph:
	def __init__(self, V):
		print "V!"
		print V
		self.adjList = [None for v in range(V)] #vertices

	def addEdge(self, vertex, edge, weight):
		if self.adjList[vertex] is None:
			self.adjList[vertex] = Node(edge, weight, None)
		else:
			firstNode = self.adjList[vertex]
			tempNode=firstNode
			while tempNode.next is not None:
				tempNode = tempNode.next
			#insert new node
			tempNode.next = Node(edge, weight, None)

	def printGraph(self):
		for i,linkedList in enumerate(self.adjList):
			print "-Vertex "+str(i)+","
			firstNode = self.adjList[i]
			tempNode=firstNode
			print(str(tempNode))
			while tempNode.next is not None:
				tempNode = tempNode.next
				print str(tempNode)


if __name__ == '__main__':
	graph = Graph(4)
	graph.addEdge(0,1,1)
	graph.addEdge(0,4,2)
	graph.addEdge(1,2,3)
	graph.addEdge(1,3,4)
	graph.addEdge(2,5,5)
	graph.addEdge(2,6,7)
	graph.addEdge(3,7,8)
	graph.addEdge(3,8,9)
	graph.addEdge(0,99,99)
	graph.printGraph()






