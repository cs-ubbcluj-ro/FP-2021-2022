"""
    Product of even numbers in a list that are on even positions
"""
import random

data = list(range(1, 10))
random.shuffle(data)
print(data)

# _enum = [y for x, y in enumerate(data) if x % 2 == 0 and y % 2 == 0]
# print(list(enumerate(data)))
#
#
# print(sum([y for x, y in enumerate(data) if x % 2 == 0 and y % 2 == 0]))


"""
    V1 - chip & conquer ( T(1) + T(n-1) )
"""


def chip_conquer(data, start):
    # past the end of the list
    if start == len(data):
        return 1

    return data[start] * chip_conquer(data, start + 1) if start % 2 == 0 and data[start] % 2 == 0 else chip_conquer(
        data,
        start + 1)


# print(chip_conquer(data, 0))

"""
    V2 - T(n/2) + T(n/2)
"""


def product_rec(data, start, end):
    if start == end:
        if start % 2 == 0 and data[start] % 2 == 0:
            return data[start]
        else:
            return 1

    middle = (start + end) // 2
    return product_rec(data, start, middle) * product_rec(data, middle + 1, end)


print(chip_conquer(data, 0))
print(product_rec(data, 0, len(data) - 1))
