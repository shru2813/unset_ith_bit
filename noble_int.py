A=list(map(int,input().split()))
def nobleInteger(A):
    A.sort()  
    n = len(A)
    for i in range(n):
        if A[i] == n - i - 1:
            return 1
    return -1
print(nobleInteger(A))