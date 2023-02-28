def check_prime(num, output = False):
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            if(output): print(f"{num} : {i}\n{num % i}")
            return False
    return True
        
prime_count = 2
n = 3

while prime_count < 10_001:
    n += 2
    if(check_prime(n)):
        prime_count += 1
        
print(n)