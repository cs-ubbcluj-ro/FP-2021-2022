"""
Alg. complexity 101

    n -> size of the program's input (length of a list, the n-th term in a sequence, side of a square)
    T(n) -> approximation of how many operations the algorithm needs for size n
    O(n) -> high bound for the number of operations

1.
    BC = AC = WC
    T(n) = n => O(n) = n, but O(n) is a high bound, so O(n) is also n^2, n^3 and so on

2.
    WC (worst case): O(n) = n
    BC (best case) : O(n) = 1

    AC (average case) : (1 + 2 + 3 + ... + n) / n = n(n+1)/2n = (n+1)/2 => O(n) = n
"""


def bs(data):
    swapped = True
    n = len(data) - 1
    while swapped:
        swapped = False
        for i in range(n):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        n -= 1


"""
    BC - list already sorted, O(n) = n (yay!)
    WC - list sorted in reverse, O(n) = n^2
        explain it:
            iteration 1 -> n - 1 swaps
            iteration 2 -> n - 2 
            ...
            iteration n - 1: 1 swap
        
"""


def merge(array_1, array_2):
    result = []
    i = 0  # array_1
    j = 0  # array_2

    while i < len(array_1) and j < len(array_2):
        if array_1[i] <= array_2[j]:
            result.append(array_1[i])
            i += 1
        else:
            result.append(array_2[j])
            j += 1

    if i < len(array_1):
        result.extend(array_1[i:])
    if j < len(array_2):
        result.extend(array_2[j:])

    return result


def merge_sort(data):
    if len(data) == 1:
        return data

    m = len(data) // 2
    # TODO Don't create list copies
    left = merge_sort(data[:m])
    right = merge_sort(data[m:])
    return merge(left, right)


"""
Time complexity of merge sort
    T(n) = 2 * T(n/2) + n/2 + n/2 = 2 * T(n/2) + n
    T(n) = 1, n <= 1

merging a list of n elems with a list of m elems is O(n,m) = n + m
    

"""

data = list(range(20))
data.reverse()
print(data)
# bs(data)
data = merge_sort(data)
print(data)
