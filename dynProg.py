#longest increasing subsequence
'''
Let arr[0..n-1] be the input array and L(i) be the length of the LIS ending at index i such that arr[i] is the last element of the LIS.
Then, L(i) can be recursively written as:
L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
L(i) = 1, if no such j exists.
To find the LIS for a given array, we need to return max(L(i)) where 0 < i < n.
Thus, we see the LIS problem satisfies the optimal substructure property as the main problem can be solved using solutions to subproblems.
'''

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
global max_lis_length

#n is the max
def longest_inc_subseq(arr, n):
	global max_lis_length

	if n is 1:
		return 1
	
	current_lis_length = 1
	for i in xrange(0, n-1):
		subproblem_lis_length = longest_inc_subseq(arr, i)

		if arr[i]<arr[n-1] and current_lis_length<(1+subproblem_lis_length):
			current_lis_length = subproblem_lis_length

	if (max_lis_length < current_lis_length):
		max_lis_length = current_lis_length

	return current_lis_length


def minStores(A):
	B = [] 
	for i in range(len(A)-1):
		dist = abs(A[i]-A[i+1])
		if dist is 2 and A[i-1] not in B and (A[i+2] not in B or A[i+1] not in B):
			mid_distance = (A[i]+A[i+1])/2
			B.append(mid_distance)
		if dist is 1 and A[i+1] not in B and A[i-1] not in B:
			B.append(A[i+1])
		if dist>2:
			B.append(A[i+1])
	print B
	return len(B)


def minStoresR(A, i, numStores):
	if len(A) is 0:
		print ("Num stores in 0: "+str(numStores))
		return numStores
	elif len(A) is 1:
		#numStores+=1
		print "Num stores in 1: "+str(numStores)
		return numStores
	if abs(A[i+1]-A[i])<=1:
		numStores+=1
		minStoresR(A[(i+2):], 0, numStores)
	elif abs(A[i+1]-A[i])>1:
		numStores+=1
		minStoresR(A[(i+1):],0,numStores)



	'''
	if n is 0:
		return 0
	if n is 1:
		return 1 #//just need 1 store for the 1 home
	if n is 2:
		if abs(A[0]-A[1])<=2:
			return 1
		else:
			return 2
	return minStoresR(A[:n/2], len(A[:n/2]))+ minStoresR(A[n/2:], len(A[n/2:]))	
	'''



if __name__ == "__main__":
	A = [1,2,3,4,5,6,7,8,9]
	#print("Should be 2 stores")
	numStores = 0
	print("FINAL")
	print(str(minStoresR(A,0,numStores)))





