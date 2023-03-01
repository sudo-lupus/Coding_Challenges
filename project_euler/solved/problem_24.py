distinct_powers = []

for i in range(2, 101):
    for j in range(2, 101):
        distinct_powers.append(i ** j)

distinct_powers = set(distinct_powers)
print(len(distinct_powers))
