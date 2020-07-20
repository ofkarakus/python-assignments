num = int(input('Enter a number : '))
prime_nums =  []

for i in range(2, num+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_nums.append(i)
print(prime_nums)


# --for içerisindeki tüm iterasyonlar bitince (exhaust = tükenince) else içerisindeki ifadeyi icra eder.
# --yani for içerisnde "break" ile iterasyon kesintiye uğramazsa eğer, eninde sonunda iterasyon bitecek ve else yapısı mutlaka icra edilecektir.
# --tabii, gene belirmek isterim ki ,for içerisnde break le iterasyon kesintiye uğratılmamışsa..