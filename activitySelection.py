'''
You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
'''
from sort import fullMergeSort
start  =  [1, 3, 0, 5, 8, 5];
finish =  [2, 4, 6, 7, 9, 9];

def sort(start, finish):
	activities = []
	sortFinish = fullMergeSort(finish)
	prevFinish = None
	for i, elem in sortFinish:
		if prev is None:
			activities.append(i)
			prevFinish = elem
		elif start[i]>prevFinish:
			activities.append(i)
			prevFinish = elem

	return activities


print(sort(start, finish))



