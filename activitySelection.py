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
	for i in range(len(sortFinish)):
		if prevFinish is None:
			activities.append(i)
			prevFinish = sortFinish[i]
		elif start[i]>prevFinish: #if the next start time is after the previous finish, aka no overlap
			activities.append(i)
			prevFinish = sortFinish[i]

	return activities


print(sort(start, finish))



