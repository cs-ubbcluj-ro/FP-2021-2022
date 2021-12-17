"""
    Computational complexity 101

    n -> size of the algorithm's input
    T(n) -> nr. of operations the algorithm makes for input of size "n"
    T(n) = n

    O(n) -> upper bound on the number of operations

1.
    T(n) = n => T(n) belongs to O(n)

2.
    T(n) between 1 and n -> depends on the structure of the input

    BC: T(n) = 1, O(n) = 1
    WC: T(n) = n, O(n) = n

5.

    T(n) = 1, n = 1
         = 4 * T(n/2) + 1
         = 4 * [ 4 * T(n/4) + 1 ] + 1


6. Binary search
    T(n) = 1, n =1
         = T(n/2) + 1


    T(n) = T(n/2) + 1 = T(n/4) + 1 + 1
"""
import random

"""
    Bubble sort
"""
data = list(range(20, 0, -1))
# random.shuffle(data)
# 20 - rabbit
# 1 - turtle

"""
WC: T(n) = (n-1) + (n-2) + ... + 2 + 1  => n^2
BC: T(n) = n
"""


def bs(data):
    swapped = True
    n = len(data) - 1

    while swapped:
        swapped = False
        print(data)
        for i in range(n):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        n -= 1


"""
    Insertion sort
"""


def insert_sort(data):
    pass


"""
    Merge sort
"""


def merge(left, right):
    i = 0  # left
    j = 0  # right
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:] + right[j:]

    # result.extend(left[i:])
    # result.extend(right[j:])
    return result


"""
    Merge Sort
    T(n) = 1, n = 1
         = 2 * T(n/2) + n
"""


def merge_sort(data):
    if len(data) == 1:
        return data

    m = len(data) // 2
    left = merge_sort(data[:m])
    right = merge_sort(data[m:])
    return merge(left, right)


print(data)
print(merge_sort(data))
# print(data,id(data))
