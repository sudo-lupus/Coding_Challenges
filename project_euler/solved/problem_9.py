def pythagorean_triplet(sum = 1000):

    for i in range(1, 998):
        for j in range(1, 998):
            c_squared = i ** 2 + j ** 2
            c = c_squared ** 0.5
            if(i + j + c == sum):
                return [i, j, c]
    return [0,0,0]

triplet = pythagorean_triplet()
print(triplet[0] * triplet[1] * triplet[2])