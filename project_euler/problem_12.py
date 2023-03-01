def get_divisors(num):
    counter = 1
    for i in range(1, (num // 2 + 1)):
        if num % i == 0:
            counter += 1
    return counter

#Naive Solution
most_divisors = 0
target_num = 0
counter = 2
current_num = 3

while(most_divisors < 500):
    current_num += counter + 1
    current_divisors = get_divisors(current_num)
    print(f"""
        Current Number : {current_num}
        Current Divisors: {current_divisors}
        Current Max: {most_divisors}
        Current Max Num: {target_num}
    """)
    if(current_divisors > most_divisors):
        most_divisors = current_divisors
        target_num = current_num
    counter += 1


print(target_num)