def same_digits(n, length = 6):
    products = [sorted([digit for digit in str(n * i)]) for i in range(1, length + 1)]
    print(f"n = {n}\nProducts = {products}")
    for product in products:
        if product == products[0]:
            continue
        else:
            return False
    return True

n = 1

while True:
    if(same_digits(n, 6)) == False:
        n += 1
    else:
        break

print(n)