def solution(N):
	bin_N = bin(N)[2:]
	ones = list()
	gaps = list()
	
#	print(type(bin_N))
#	print(bin_N)
	
	for i in range(len(bin_N)):
		if bin_N[i] == '1':
			ones.append(i)

#	print(ones)
	
	if len(ones) > 1:
		for i in range(len(ones)-1):
			gap = (ones[i+1] - ones[i])-1
			gaps.append(gap)
	
	else: gaps.append(0)
		
#	print(gaps)
	
	return max(gaps)

if __name__ == '__main__':
	
	value = solution(4)

	print(value)