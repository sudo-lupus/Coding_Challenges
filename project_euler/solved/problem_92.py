def square_digits(n):
    if n == 89 or n == 1:
        return n
    else:
        return square_digits(sum([int(i) ** 2 for i in str(n)]))

import time

counter = 0

st = time.time()
end_list = set()

for i in range(1, 10 ** 7):
    if(square_digits(i) == 89):
        counter += 1

et = time.time()
elapsed_time = et - st
print(counter)
print('Execution time:', elapsed_time, 'seconds')