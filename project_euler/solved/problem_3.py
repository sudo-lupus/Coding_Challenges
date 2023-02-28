'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def check_prime(num, output = False):
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            if(output): print(f"{num} : {i}\n{num % i}")
            return False
    return True

a = 600851475143

n = int(a ** 0.5) + 1

while True:
    if n % 2 == 0:
        n -= 1
    if(check_prime(n, output = True) and a % n == 0):
        break
    else:
        n -= 2

    if(n <= 2):
        break
    
print(n)