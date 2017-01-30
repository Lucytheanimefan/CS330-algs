original_A = [1,2,3,9,8,4,5,6,7,10,11,12,13,14,15]


def find_pivot(A):
	c = [] #medians
	fifth = len(A)/5
	A1 = A[0:fifth]
	A2 = A[fifth:2*fifth]
	A3=A[2*fifth:3*fifth]
	A4 = A[3*fifth: 4*fifth]
	A5 = A[4*fifth:]
	print("As--------")
	print(A1)
	print(A2)
	print(A3)
	print(A4)
	print(A5)
	print("------------")
	print(fifth/2)
	c.append(A1[selection(A1, fifth/2)])
	c.append(A2[selection(A2, fifth/2)])
	c.append(A3[selection(A3, fifth/2)])
	c.append(A4[selection(A4, fifth/2)])
	c.append(A5[selection(A5, fifth/2)])
	print("C: ")
	print(c)
	return selection(c, fifth/2)


#need to sort too!
#index of kth smallest element in A
def selection(A, k):
	print("SELECTION CALLED")
	index = int(len(A)/2)
	print("index 0: "+str(index))
	p = A[index]
	print("Pivot: ")
	#return
	print(p)
	A2 = p
	A1 = []
	A3=[]
	for i in range(len(A)):
		if A[i]<p:
			A1.append(A[i])
		elif A[i]>p:
			A3.append(A[i])
	if k < index:
		return selection(A1, k)
	elif A[index] is original_A[k]:
		print("FOUND IT: "+str(p))
		return p
	elif k > index:
		print("k>index: ")
		print(A3)
		print(k)
		return selection(A3, k)



print(selection(original_A,4))
#print(find_pivot(A))