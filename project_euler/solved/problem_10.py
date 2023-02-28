def check_prime(num, output = False):
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            if(output): print(f"{num} : {i}\n{num % i}")
            return False
    return True

sum = 2
for i in range(3, 2_000_000, 2):
    if(check_prime(i)): 
        sum += i
        print(i)

print(f"The sum of all primes up to 2 million is {sum}")