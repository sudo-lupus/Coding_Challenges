largest = 0
comb = [0,0]

for i in range(999, 100, -1):
    for j in range(999, 100, -1):

        #Integer with 5 digits can not be a palindrome
        if(i * j < 100000):
            break

        product = i * j
        if(product < largest):
            break

        #Convert product to a string and check if first 3 digits are equal to last 3 reversed digits
        product_string = str(product)
        if(product_string[0:3] == product_string[:2:-1]):
            if(product > largest):
                comb[0] = i
                comb[1] = j
                largest = product
            break

print(largest)
print(comb)