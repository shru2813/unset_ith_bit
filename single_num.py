nums = list(map(int, input().split()))
u = 0
for num in nums:
    u^= num

print(u)