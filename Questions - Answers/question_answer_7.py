# Define a function with 'arbitrary numbers of arguments' method named as ‘spec_opr
# (*numbers)’ . This function sums all of the arguments after a process. This process 
# is even numbers should be divided by 2 and odd numbers should be multiplied with 3 
# first and then added to the total sum.
# Examples:
# spec_opr(3, 2, 6) should return 13,
# spec_opr(58, 53, 10, -10, -40, -28, 8, 34, 70, -16, 33) should return 301,
# spec_opr(93, 12, 5, 84, -22) should return 331

# first answer

def spec_opr1(*numbers):
    return round(sum(tuple(map(lambda x : x/2 if x % 2 == 0 else x * 3, numbers))))

# second answer

def spec_opr2(*numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number/2
        else:
            total += number*3
    return int(total)

# tests

print(spec_opr1(3, 2, 6))
print(spec_opr1(58, 53, 10, -10, -40, -28, 8, 34, 70, -16, 33))
print(spec_opr1(93, 12, 5, 84, -22))

print(spec_opr2(3, 2, 6))
print(spec_opr2(58, 53, 10, -10, -40, -28, 8, 34, 70, -16, 33))
print(spec_opr2(93, 12, 5, 84, -22))