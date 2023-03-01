def get_next_fibonacci(f1, f2):
    return f1 + f2

f1 = 1
f2 = 1
index = 2

while(f1 < 10 ** 999):
    temp_f1 = f1
    f1 = f1 + f2
    f2 = temp_f1
    index += 1

print(len(str(f1)))
print(index)