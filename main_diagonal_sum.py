n=int(input())
m=int(input())
mat=[]
for i in range(n):
    d=[]
    for j in range(m):
        d.append(int(input()))
    mat.append(d)
sum=0 
for i in range(n):
    sum+=mat[i][i]
print(sum) 