


def knapsack(val, wt, W, i):
	if i is 0 or W is 0:
		return 0
	if wt[i-1]>W:
		return knapsack(val, wt, W - wt[i-1], i-1)
	else:
		return max(val[i-1] + knapsack(val, wt, W-wt[i-1], i-1),
			knapsack(val, wt, W - wt[i-1], i-1))


if __name__ == "__main__":
	val = [60, 100, 120]
	wt = [10, 20, 30]
	W = 50

	print(knapsack(val, wt, W, len(val)))

	print("Should be: "+str(220))
