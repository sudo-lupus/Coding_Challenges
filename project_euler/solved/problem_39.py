
solutions = [0 for i in range(1,1001)]

for i in range(1,1001):
    for j in range(1, 1001):
        c = (i ** 2 + j ** 2) ** 0.5
        if c % 1 == 0 and i + j + c <= 1000:
            solutions[int(i + j + c) -1] += 1

print(solutions.index(max(solutions)) + 1)