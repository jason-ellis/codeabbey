"""
Sum of digits
Problem #11
http://www.codeabbey.com/index/task_view/sum-of-digits

This programming exercise is intended to introduce numeral system basics to you. We start learninig this concept by playing with decimal system which we use everyday (though you should keep in mind that computer does not use it internally - it only converts numbers to it when they should be shown to user).

As any number greater than 9 is represented by several digits, we can calculate the sum of these digits. For example, for numbers 1492 and 1776 we get:

1 + 4 + 9 + 2 = 16
1 + 7 + 7 + 6 = 21
In this task you will be given several numbers and asked to calculate their sums of digits.

Important: while many programming languages have built-in functions to convert numbers to strings (from which digits could be extracted), you should not use this (since your goal is to learn some programming tricks).

Instead you need to implement algorithm with repetitive division by 10 (base of numeral system) and summing up the remainders. Read the Number to digits article for details on the algorithm.

Problem statement

Input data are in the following format:

first line contains N - the number of values to process;
and then N lines will follow describing the values for which sum of digits should be calculated by 3 integers A B C;
for each case you need to multiply A by B and add C (i.e. A * B + C) - then calculate sum of digits of the result.
Answer should have N results, also separated by spaces. For example:
"""
count = int(input())

results = []

for i in range(count):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    result = a * b + c
    num_set = []
    while result > 0:
        rem = int(result % 10)
        result = int(result / 10)
        num_set.append(rem)
    sum = 0
    for i in num_set:
        sum += i
    results.append(str(sum))

print(' '.join(results))