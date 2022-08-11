from array import array

# Handling 6 bytes of memory as 1×6, 2×3, and 3×2 views
octets = array('B', range(6))

m1 = memoryview(octets)
m1.tolist()  # [0, 1, 2, 3, 4, 5]

m2 = m1.cast('B', [2, 3])
m2.tolist()  # [[0, 1, 2], [3, 4, 5]]

m3 = m1.cast('B', [3, 2])
m3.tolist()  # [[0, 1], [2, 3], [4, 5]]

m2[1,1] = 22
m3[1,1] = 33


# Changing the value of a 16-bit integer array item by poking one of its bytes

numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
len(memv) # == len(numbers), 5
memv[0] # == numbers[0], -2

memv_oct = memv.cast('B')
memv_oct[5] = 4
print(numbers) # array('h', [-2, -1, 1024, 1, 2]), vakyes are now corrupted