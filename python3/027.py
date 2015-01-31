"""
Bubble Sort
Problem #27
http://www.codeabbey.com/index/task_view/bubble-sort

Array sorting is a popular problem for programming newcomers - and extremely important thing in professional programming (in databases, libraries etc).

Sorting is reordering according to some simple rule based on comparison. Suppose we are given an array:

a = [3, 1, 4, 1, 5, 9, 2, 6]
and we want its elements to be reordered in non-decreasing order - i.e. if one element is placed earlier (to the left) than the other - we can be sure the first element is either less or equal to second.

Mathematically speaking, for any indexes i and j if i < j then a[i] <= a[j].

Bubble Sort is one of the simplest methods to perform such reordering. We will describe it in even simpler way than usual:

Take a pass through array, examining all pairs of adjacent elements (N-1 pairs for array of N elements).
If in any pair with indexes i and i+1 the condition a[i] <= a[i+1] does not hold, swap these two elements.
Repeat such passes through array until the new pass will do no swaps at all.
It is obvious, that if the pass do not perform any swaps, the array is already sorted and future passes could not change anything.

To swap elements with indexes i and j there are few variants. For example temporary variable t could be used:

t = a[i]
a[i] = a[j]
a[j] = t
Input data will contain array size in first line and array itself in the second (integer values separated with spaces).
Answer should contain two values - number of passes perfromed and total number of swaps made. For example:
"""
count = int(input())

array = input().split()

array = [int(x) for x in array]

passes = 0
swaps = 0

while True:
    swap_count = swaps
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            t = array[i]
            array[i] = array[i+1]
            array[i+1] = t
            swaps += 1
    passes += 1
    if swap_count == swaps:
        break

print(passes, swaps)