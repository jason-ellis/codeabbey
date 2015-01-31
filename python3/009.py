"""
Triangles
Problem #9
http://www.codeabbey.com/index/task_view/triangles

Triangle is an object built of three line segments (sides of triangle), connected by ends. Wiki on triangles provides more detailed explanation.
If we have three line segments with lengths A B C - we either can built a triangle with them
(for example with 3 4 5 or 3 4 7 - though this is with zero area) or we found it impossible
(for example 1 2 4).

You are given several triplets of values representing lengths of the sides of triangles. You should tell from which triplets it is possible to build triangle and for which it is not.

Input data: First line will contain number of triplets.
Other lines will contain triplets themselves (each in separate line.
Answer: You should output 1 or 0 for each triplet (1 if triangle could be built and 0 otherwise).
"""
count = int(input())

results = []

for i in range(count):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    if a > b + c:
        results.append(0)
    elif b > a + c:
        results.append(0)
    elif c > a + b:
        results.append(0)
    else:
        results.append(1)

results = [str(i) for i in results]
print(' '.join(results))