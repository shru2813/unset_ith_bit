a=list(map(int,input().split()))
a=sorted(a)
d=(a)[::-1]
cost=0
for i in range(len(d)):
    cost=cost+d[i]*(i+1)
print(cost)