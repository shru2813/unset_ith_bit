a=list(map(int,input().split()))
s=len(a)
p=1
sum=0
while(s):
    sum+=((a[s-1]%3)*(p))%3
    p=(10*p)%3
    s=s-1
if (sum%3==0):
    print('1')
else:
    print('0')    