from sort import fullMergeSort
import tree
from tree import *

arr = ["9:00",  "9:40", "9:50",  "11:00", "15:00", "18:00"]
dep  = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

new_arr = [int(x.replace(":",".")) for x in arr]
new_dep = [int(x.replace(":",".")) for x in arr]

def createTree(arr, dep):
	tree = BinaryTree()

	for i in range(len(dep)):
		tree.insert(i,)
	tree.insert(5)
	tree.insert(7)
	tree.insert(4)
	tree.insert(6)
	tree.insert(3)

def intervalPartition(arr, dep):
	lecs = 0
	
	sort_arr = fullMergeSort(new_arr);
	for i in range(len(dep)):
		if (new_dep[i-1]>new_arr[i]):




