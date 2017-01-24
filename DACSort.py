def find_pivot(A):
	c = [] #medians
	fifth = len(A)/5
	A1 = A[0:fifth]
	A2 = A[fifth:2*fifth]
	A3=[2*fifth:3*fifth]
	A4 = [3:fifth: 4*fifth]
	A5 = [4*fifth]
	c.push(selection(A1, 3))
	c.push(selection(A2, 3))
	c.push(selection(A3, 3))
	c.push(selection(A4, 3))
	c.push(selection(A5, 3))
	return selection(c, 3)


#kth smallest element in A
def selection(A, k):
	p = find_pivot(A)
	print("Pivot: ")
	print(p)
	A1 = A[0:p]
	A2 = A[p]
	A3 = A[p+1:]
	if k < p:
		return selection(A1, k)
	elif k is p:
		return p
	elif k > p:
		return selection(A3, k)


A = [1,2,3,9,8,4,5,6,7]
print(selection(A,4))