def solution(A,k):

    for n in range(k):
        
        temp = A[len(A)-1]
        #i = len(A)-1
        
        #while i > 0:
        for i in range(len(A)-1,0,-1):
            A[i] = A[i-1]
            #i-=1
            
        A[0] = temp

        
    return A

if __name__ == '__main__':

    A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    k = 20
    value = solution(A,k)

    print(value)
