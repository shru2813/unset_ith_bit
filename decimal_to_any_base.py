n = int(input())
m= int(input())
result = ""

while n> 0:
    r = n % m
    result = str(r) + result
    n //= m

print(result)