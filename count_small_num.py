lst=list(map(int,input().split()))
d=[]
for i in range(len(lst)):
    count=0
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            count=count+1
    d.append(count)        
print(d)