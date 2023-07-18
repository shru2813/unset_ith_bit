n=int(input())
m=int(input())
mat=[]
for i in range(n):
    a=[]
    for j in range(m):
        a.append(int(input()))
    mat.append(a)
tran=[]    
for row in zip(*mat):
    tran.append(row)
result=[]
for row in tran:
    str=row[::-1]
    result.append(str)
print(result) 