n=int(input())
m=int(input())
mat=[]
for i in range(n):
    a=[]
    for j in range(m):
        a.append(int(input()))
    mat.append(a)
t=0
result=[]
for i in range(n):
    s=[]
    for j in range(m):
        if i<j:
            t=mat[i][j]
            mat[i][j]=mat[j][i]
            mat[j][i]=t
        s.append(mat[i][j])      
    result.append(s)   
print(result)