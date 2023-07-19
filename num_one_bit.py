def count_bits(n):
    count = 0

    while n > 0:
        if n & 1:
            count += 1
        n >>= 1

    return count
num = int(input("Enter an integer: "))
result = count_bits(num)
print(result)