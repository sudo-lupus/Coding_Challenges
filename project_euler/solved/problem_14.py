def get_next_num(num):
    if num % 2 == 0:
        return (num // 2)
    else:
        return (3 * num + 1)
    
def get_collatz_length(num):
    counter = 1

    while(num > 1):
        num = get_next_num(num)
        counter += 1

    return counter

max_length, max_num = 0, 0

for i in range(1, 1_000_000):
    current_length = get_collatz_length(i)
    print(f"{i} : {current_length}")
    if current_length > max_length: 
        max_length = current_length
        max_num = i

print(max_num)
