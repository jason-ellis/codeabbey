"""
Sum in Loop
Problem #2
http://www.codeabbey.com/index/task_view/sum-in-loop

Now your goal is to learn programming loops - i.e. repeated actions. You are to find sum of several numbers (more than two). It will be useful to do this in loop. Perhaps "for" loop will suit nicely since the amount of values for summation is given.

Input data has the following format:

first line contains N - amount of values to sum;
second line contains N values itself.
Answer should contain a single value - the sum of N values.
"""
numbers = []
count = input()
numbers = input().split()

sum = 0

for n in numbers:
    sum += int(n)

print(sum)