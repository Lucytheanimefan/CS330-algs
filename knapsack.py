

#O(2^n)
def knapsack(val, wt, W, i):
	if i is 0 or W is 0:
		return 0
	if wt[i-1]>W:
		return knapsack(val, wt, W - wt[i-1], i-1)
	else:
		return max(val[i-1] + knapsack(val, wt, W-wt[i-1], i-1),
			knapsack(val, wt, W - wt[i-1], i-1))


#O(nW)
def dyn_knapsack(val, wt, W):
	n = len(val)
	store = [[0 for x in range(W+1)] for y in range(n+1)]
	#print store
	for i in range(n+1):
		for w in range(W+1):
			if i is 0 or w is 0:
				#print store[i][w]
				store[i][w] = 0
			elif wt[i-1]<=w:
				store[i][w] = max(val[i-1] + store[i-1][w-wt[i-1]],store[i-1][w])
			else:
				store[i][w] = store[i-1][w]

	for row in store:
		print row
				
	return store[n][W]


if __name__ == "__main__":
	val = [60, 100, 120]
	wt = [10, 20, 30]
	W = 50

	#print(knapsack(val, wt, W, len(val)))
	print(dyn_knapsack(val, wt, W))

	print("Should be: "+str(220))
