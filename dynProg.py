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
	elif abs(A[i+1]-A[i])>1 and abs(A[i+1]-A[i])<=2:
		numStores+=1
		minStoresR(A[(i+1):],0,numStores)


def edit_distance(word1, word2):
	n = len(word1)
	m = len(word2)
	if word1 is word2:
		return 0
	if m is 0:
		return n
	if n is 0:
		return m
	if word1[n-1] is word2[m-1]: #last characters are the same
		return edit_distance(word1[:n-1], word2[:m-1])
	else:
		return 1+ min(edit_distance(word1[:n-1], word2[:m-1]), 
			edit_distance(word1[:n-1],word2[:m]), 
			edit_distance(word1[:n], word2[:m-1]))




if __name__ == "__main__":
	A = [1,3,5,7,9]
	#print("Should be 2 stores")
	numStores = 0
	
	print (edit_distance("sunday","saturday"))





