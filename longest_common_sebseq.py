

#naive version
def lcs(seq1, seq2):
	m = len(seq1)
	n = len(seq2)

	to_ret = [[None]*(n+1) for y in range(m+1)]
	#print to_ret

	#i=0
	#j=0
	for i in range(m+1):	
		for j in range(n+1):
			print str(i)+", "+str(j)  
			if i is 0 or j is 0:
				to_ret[i][j] = 0
			elif seq1[i-1] is seq2[j-1]:
				print str(seq1[i-1])+" is "+str(seq2[j-1])+"?"
				to_ret[i][j] = to_ret[i-1][j-1]+1
				#to_ret.append(c)
			else:
				print "max: "+str(to_ret[i-1][j]) +" vs "+str(to_ret[i][j-1])
				to_ret[i][j] = max(to_ret[i-1][j],to_ret[i][j-1])
			#j+=1
		#i+=1
		#
	print to_ret
	return to_ret[m][n]




if __name__ == "__main__":
	seq1 = 'AGGTAB'
	seq2 = 'GXTXAYB'
	print lcs(seq1, seq2)
