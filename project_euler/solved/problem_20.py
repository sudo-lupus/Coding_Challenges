def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

string_prod = str(factorial(100))
digits = [int(digit) for digit in string_prod]
sum_digits = sum(digits)


print(sum_digits)