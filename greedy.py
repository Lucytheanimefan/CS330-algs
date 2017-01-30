'''
Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline. It is also given that every job takes single unit of time, so the minimum possible deadline for any job is 1. How to maximize total profit if only one job can be scheduled at a time.
'''
from operator import itemgetter
def jobSequence(jobs):
	sort_jobs = sorted(jobs, key=itemgetter(1)) 
	print(sort_jobs)
	n = len(sort_jobs)
	results = []
	maxProf = sort_jobs[-1][2]
	maxJob = None
	while len(sort_jobs)>1:
		job = sort_jobs.pop()
		print("Popped job: "+ str(job))
		last = sort_jobs[-1]
		if job[1] is last[1]:
			print(str(job) + " is " + str(last))
			print("current maxProf"+str(maxProf))
			if job[2]>last[2] and job[2]>=maxProf:
				maxProf = job[2]
				maxJob = job
				print("MAX JOB: "+str(maxJob))
			elif last[2]>job[2] and last[2]>=maxProf:
				maxProf = last[2]
				maxJob = last
			if len(sort_jobs) is 1: #only do for the last job
				print("APPEND "+str(maxJob)+ "as last element")
				results.append(maxJob)

		elif job[1] is not last[1]: #diff deadline
			print("Append: "+str(job))
			results.append(job)
			maxProf = last[2]
			maxJob = last

	print(results)
	return results

def minimizeCash(cash):
	n = len(cash)
	netCash = {k:0 for k in range(n)}
	print(netCash)
	for i in range(n):
		for j in range(n):
			netCash[j] = cash[i][j] + netCash[j]
			netCash[i] = netCash[i] - cash[i][j]


	print netCash






if __name__ == "__main__":
	#job, deadline, profit
	jobs = [ ['a', 2, 100], ['b', 1, 19], ['c', 2, 27], ['d', 1, 25], ['e', 3, 15],['f', 1, 35],['g', 4, 25],['h', 4, 15]]
	#jobSequence(jobs)

	cashes = [[0, 1000, 2000],[0, 0, 5000],[0, 0, 0]];
	#{0: -3000, 1: -4000, 2: 7000}

	minimizeCash(cashes)
