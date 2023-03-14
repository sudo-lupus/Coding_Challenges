'''
The Hyperfactorial

Your task
Implement a function hyperfact(num) that takes a positive integer num and returns the hyperfactorial of it.

In order for your answer not to be too messy (hyperfactorial of 100 is 9015 digits long) give the answer modulo 1000000007.

Notes
1 <= n <= 300

50 random tests
'''

def hyperfact(num):
    my_sum = 1
    for i in range(1, num+1):
        my_sum *= i ** i
    return my_sum % 1000000007