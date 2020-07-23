# Task : Print the prime numbers which are between 1 to entered limit number (n).

# You can use a nested for loop.
# Collect all these numbers into a list

num = int(input('Enter the limit number : '))
prime_nums = []

for i in range(2, num+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_nums.append(i)
print(prime_nums)


# --for içerisindeki tüm iterasyonlar bitince (exhaust = tükenince) else 
# içerisindeki ifadeyi icra eder.
# --yani for içerisnde "break" ile iterasyon kesintiye uğramazsa eğer, eninde 
# sonunda iterasyon bitecek ve else yapısı mutlaka icra edilecektir.
# --tabii, gene belirmek isterim ki ,for içerisnde break le iterasyon kesintiye 
# uğratılmamışsa..

# ================================================================================

# second solution

n = int(input("Enter the limit number: "))
prime = []
for num in range(2, n+1):
    status = True
    for i in range(2, num):
        if num % i ==0:
            status = False
    if status:
        prime.append(num)
print(prime)