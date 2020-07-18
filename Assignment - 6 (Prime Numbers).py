num = int(input())
prime_nums =  []

for i in range(1, num+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_nums.append(i)
print(prime_nums)