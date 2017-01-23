import math
#it works :)
def insertionsort(toSort):
	#sortedList = [];
	#sortedList.append(toSort[0])
	for i in range(len(toSort)):
		for j in range(i):
			while (toSort[i]<toSort[j] and i>0):
				temp = toSort[i]
				toSort[i]=toSort[j]
				toSort[j] = temp

	return toSort


def mergesort(B, iBegin, iEnd, A):
	if (iEnd - iBegin < 2):
		print("LESS THAN 2")
		return 
	iMiddle = (iEnd + iBegin)/2
	mergesort(A, iBegin, iMiddle, B)
	mergesort(A, iMiddle, iEnd, B)
	A = merge(B, iBegin, iMiddle, iEnd, A)
	return A
	

def merge(A, iBegin, iMiddle, iEnd, B):
	print("MERGE")
	i = iBegin
	j = iMiddle
	for z in range(iEnd - iBegin):
		k = z + iBegin
		if (i<iMiddle and (j>=iEnd or A[i]<=A[j])):
			B[k]=A[i]
			i = i+1
		else:
			B[k]=A[j]
			j=j+1
	return B

		

def fullMergeSort(A):
	B = list(A)
	n = len(A)
	print(A)
	print(B)
	print(n)
	return mergesort(B,0,n,A)


def bSearch(hi, lo, target, sortedList):
	print("TARGET: "+str(target))
	mid = int(math.floor((hi+lo)/2))
	print("Mid: "+str(mid))
	print("Value at mid: "+str(sortedList[mid]))
	print(type(sortedList[mid]))
	if target==sortedList[mid]:
		print("FOUND TARGET at "+str(mid))
		return mid
	elif target<sortedList[mid]:
		print("target less than sortedlist at mid")
		print(str(target)+"<"+str(sortedList[mid]))
		bSearch(0,mid,target,sortedList)
	elif target>sortedList[mid]:
		print("target larger than sortedlist at mid")
		bSearch(mid-1, len(sortedList)+1, target,sortedList)


def binarySearch(sortedList, target):
	hi = len(sortedList)
	lo = 0
	return bSearch(hi, lo, target, sortedList)




someList = [1,2,6,9,14,22,99]
#print(insertionsort(someList))
#
print(binarySearch(someList,1))

