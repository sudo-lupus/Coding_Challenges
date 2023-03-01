digit_sum = 0

for i in range(1000, 1000000):
    i_digits = [int(digit) for digit in str(i)]
    i_digits_power5 = [digit ** 5 for digit in i_digits]
    if sum(i_digits_power5) == i:
        print(i_digits)
        digit_sum += i

print(digit_sum)