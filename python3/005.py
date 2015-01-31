"""
Minimum of Three
Problem #5
http://www.codeabbey.com/index/task_view/min-of-three

To have more practice with conditional statements we are going to write a program which uses complex condition. I.e. one if ... else statement could be (and should be) nested inside other to solve this problem.

Several triplets of numbers are given to you. Your task is to select minimum among each of triplets.

Input data will contain in the first line the number of triplets to follow.
Next lines will contain one triplet each.
Answer should contain selected minimums of triplets, separated by spaces.
"""
count = int(input())

output = []

for i in range(count):
    a, b, c = input().split()
    if int(a) < int(b):
        if int(a) < int(c):
            output.append(a)
        else:
            output.append(c)
    else:
        if int(b) < int(c):
            output.append(b)
        else:
            output.append(c)

print(' '.join(output))