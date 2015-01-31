"""
Greatest Common Divisor
Problem #26
http://www.codeabbey.com/index/task_view/greatest-common-divisor

It looks like none of beginner's courses on programming avoids practicing Euclid's algorithm for calculation of the greatest common divisor of two numbers. Let us not deviate from this popular trend and study this puzzle too, though it is mostly important in number theory (which in its turn has great importance in cryptography).

For explanation of the algorithm needed for this task please refer to the GCD and LCM article.

The task

Input data contain number of test-cases in the first line.
Then lines with test-cases follow, each containing two numbers - for A and B.
Answer should contain GCD and LCM for each pair, surrounded by brackets and separated by spaces, for example:
"""
count = int(input())

def find_gcd(a, b):
    while a is not b:
        if a > b:
            a -= b
        if b > a:
            b -= a
    return a

def find_lcm(a, b, gcd):
    lcm = a * b / gcd
    return int(lcm)

for i in range(count):
    a, b = input().split()
    a, b = int(a), int(b)
    gcd = find_gcd(a, b)
    lcm = find_lcm(a, b, gcd)
    print("({} {}) ".format(gcd, lcm))