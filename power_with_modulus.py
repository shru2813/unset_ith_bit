A=int(input())
B=int(input())
C=int(input())
pro=1
for i in range(B):
    A=A%C
    pro*=A
print(pro%C) 