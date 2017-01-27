from sort import fullMergeSort
import tree
from tree import *

arr = ["9:00",  "9:40", "9:50",  "11:00", "15:00", "18:00"]
dep  = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]


new_dep = [float(x.replace(":",".")) for x in arr]
new_arr = [float(x.replace(":",".")) for x in arr]

def intervalPartition(arr, dep):
	count = 1
	result = 1
	j=0
	i = 1
	n = len(arr)
	new_dep = [float(x.replace(":",".")) for x in dep]
	new_arr = [float(x.replace(":",".")) for x in arr]
	print new_dep
	print new_arr
	while i<n and j<n:
		#i is number of arrivals
		if new_arr[i]<new_dep[j]:
			count = count + 1
			i = i+1
			if count>result:
				result = count
		else:
			count = count-1
			j=j+1 #j is number of departures

	print("Num trains: ")
	return result

if __name__ == "__main__":

	print(intervalPartition(arr,dep))