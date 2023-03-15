'''
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
'''

def snail(array):
    snail_track = []
    counter = 0
    try:
        while True and (counter < 10000):
            snail_track.extend(array[0])
            array.pop(0)

            for arr in range(len(array[:-1])):
                snail_track.append(array[arr][-1])
                array[arr].pop(-1)
                
            snail_track.extend(array[-1][::-1])
            array.pop(-1)

            for arr in range(len(array))[::-1]:
                snail_track.append(array[arr][0])
                array[arr].pop(0)
            counter += 1
    except IndexError: return snail_track