def is_prime(num, output = False):
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            if(output): print(f"{num} : {i}\n{num % i}")
            return False
    return True

counter = 9
searching = True
while searching:
    for i in range(1, counter + 1):
        primes = [i for i in range(1,9) if is_prime(i)]
        squares = [i ** 2 for i in range(1,int(9 ** 0.5) + 1)]
        for k in primes:
            for j in squares:
                if i == k + j:
                    break