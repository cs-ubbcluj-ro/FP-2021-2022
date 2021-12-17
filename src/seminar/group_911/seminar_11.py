"""
    Computational complexity

    n -> size of the algorithm's data
    T(n) -> number of steps taken by the algorithm

    O(n) -> upper bound on the complexity

1.
    T(n) = n (for loop of 1 operation which runs n times)

2.
    BC: T(n) = 1, T(n) in O(1) (element always found on first position)
    WC: T(n) = n, T(n) is O(n) (elements not in the array)

3.
    T(n) = n^2 * n^2, O(n^4) (n^2 outer loop, n^2 inner while loop)

4.
    T(n) = n^2 * log_10(n^2), O(n^2 * log_10(n))

5.
    T(n) = 1, n = 1
         = 4 * T(n/2) + 1, n > 1

    T(n) = 4 * T(n/2) + 1 = 4 * [ 4 * T(n/4) + 1 ] + 1 ...

6.
    T(n) = 1, n = 1
         = T(n/2) + 1, n > 1

    T(n) = T(n/2) + 1 = T(n/4) + 1 + 1 = T(n/8) + 1 + 1 + 1, n = 2^k, T(n) ~ log_2(n)
"""

"""
    WC: T(n) = (n - 1) + (n - 2) + ... + 2 + 1 => O(n^2)
"""


def bubble_sort(data):
    swapped = True
    k = 1
    while swapped:
        swapped = False
        print(data)
        for i in range(len(data) - k):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        k += 1


def insert_sort(data):
    for i in range(1, len(data)):
        j = i - 1
        val = data[i]
        while j >= 0:
            if val < data[j]:
                data[j + 1] = data[j]
            else:
                break
            j -= 1
        data[j + 1] = val


"""
    WC: T(n) = 1 + 2 + 3 + ... + n-1 => O(n^2)
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

    # result += left[i:] + right[j:]
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(data):
    if len(data) == 1:
        return data

    m = len(data) // 2
    left = merge_sort(data[:m])
    right = merge_sort(data[m:])

    return merge(left, right)


"""
    T(n) = 1, n = 1
         = 2 * T(n/2) + n
"""

data = list(range(20, 0, -1))
print(data)
data = merge_sort(data)
print(data)
