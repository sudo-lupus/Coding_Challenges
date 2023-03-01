def is_pandigital(num):
    num_string = str(num)
    digits = [digit for digit in num_string]
    print(digits)
    for i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if i not in digits:
            return False
    return True
    unique_digits = set([int(digit) for digit in num_string])
    return len(unique_digits) == 10

print(10**9)
pan_digits = []

def gen_pan_digits():
    digits = [str(i) for i in range(0,10)]
    pan_digits = []
