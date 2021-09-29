"""
FP seminar 1 problems & solutions

git
    - system & software for source code management (provides commit, push and many other operations)
    - has a command line tool for almost all OSs

GitHub
    - platform for working with source code that is managed using git
    - provides in the cloud git repositories

GitHubDesktop
    - desktop application that makes working with git & GitHub easy :)

PyCharm
    - Python development environment
    - Provides tools to work with git (linked to GitHub or any other git repo)
"""

"""
1. Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10
Question – What happens if we enter a non-integer number, or alphanumeric characters?
"""


# Here we declared the function (we don't call it)
def one_is_ten(first, second):
    # Assignment (or 'binding') transfers both the TYPE and the VALUE of the variable (right to left side)
    return first == 10 or second == 10 or (first + second == 10)


a = int(input("Enter a"))
b = int(input('Enter b'))

print(one_is_ten(a, b))

"""
2. Write a Python program which iterates the integers from 1 to 50. 
For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".

FizzBuzz over the top: https://www.tomdalling.com/blog/software-design/fizzbuzz-in-too-much-detail/
"""

"""
3. Calculate the first n terms of the Fibonacci sequence
"""

"""
3. Write a Python program to calculate body mass index.
Question - How do we validate the code above for user input?
++ Let's write the specification for it
"""

"""
4. Given a non-empty string like "Code" return a string like "CCoCodCode"
    stringSplosion('Code') → 'CCoCodCode'
    stringSplosion('abc') → 'aababc'
    stringSplosion('ab') → 'aab'
"""

"""
5. Given 2 strings, a and b, return the number of the positions where they contain the same length 2
substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the
same place in both strings.
    stringMatch('xxcaazz', 'xxbaaz') → 3
    stringMatch('abc','abc) → 2
    stringMatch('abc', 'axc') → 0
"""

"""
6. Write a Python program to remove all duplicate elements from a given array and returns a new array.
"""

"""
7. Return the sum of the numbers in a list, returning 0 for an empty list. Except the number 13 is very
unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
"""
