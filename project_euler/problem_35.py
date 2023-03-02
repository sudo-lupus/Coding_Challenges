import itertools

def is_prime(num, output = False):
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            if(output): print(f"{num} : {i}\n{num % i}")
            return False
    return True

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

primes = []

for i in range(2, 10 ** 6):
    if(is_prime(i)): 
        primes.append(str(i))

circular_primes = []

print(primes[1000])
prime_candidates = []

for i in itertools.permutations("11", 2):
    prime_candidates.append(i)
    print(i)
print(set(prime_candidates))
