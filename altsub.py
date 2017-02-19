def altseq(A):
	a = len(A)
	arr = [0 for i in range(len(A))]
	for i in range(a):
		print i

		if i is 0:
			A[i]=0
		elif i is a-1:
			arr[i] = arr[i-1]
		elif (A[i-1]>A[i] and A[i+1]>A[i]) or (A[i-1]<A[i] and A[i-1]<A[i]):
			print "Increment by 1!"
			arr[i] = arr[i-1]+1
	print arr
	return arr[len(arr)-1]



A = [1,2,3,4,2,5,4,6,0,1]

print(altseq(A))