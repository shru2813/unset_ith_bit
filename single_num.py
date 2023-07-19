A = list(map(int, input("Enter the array of integers: ").split()))

unique_num = 0
for num in A:
    unique_num ^= num

print(unique_num)