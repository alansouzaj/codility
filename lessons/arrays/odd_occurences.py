from collections import Counter

def solution(A):
	
	z = Counter(A)
	
	for x,y in z.items():
		if (y%2) != 0:
			value = int(x)
	
	return value

if __name__ == '__main__':
	
	A = [1,2,3,1,2,3,4,4,4,4,5]
	value = solution(A)

	print(value)