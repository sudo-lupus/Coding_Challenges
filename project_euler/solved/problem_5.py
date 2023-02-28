'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

n = 20
found_smallest = False

while found_smallest == False:
    if all(n % i == 0 for i in range(1, 21)):
        found_smallest = True
        break
    n += 20

print("The smallest integer (larger than 20) which is evenly divisible by all the integers from 1 to 20 is:", n)
