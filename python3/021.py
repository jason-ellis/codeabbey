"""
Array Counters
Problem #21
http://www.codeabbey.com/index/task_view/array-counters

From this problem you may learn a useful programming trick used in many variants of statistic calculations.

Imagine that some forester is trying to count pines, firs and birches on the some section of wood. He can go through this section three times, counting only pines on first pass, only firs on the second and only birches on the third.

More efficient way is to make only one pass through wood and for each tree add a dot to one of tree pages in his notebook - the first page for pines, next for firs and last for birches. That is the idea of counting similar elements in the sequence using array of counters (instead of notebook).

Here is an array of length M with numbers in the range 1 ... N, where N is less than or equal to 20. You are to go through it and count how many times each number is encountered.
I.e. it is like Vowel Count task, but you have to maintain more than one counter. Be sure to use separate array for them, do not create a lot of separate variables, one for each counter.

Input data contain M and N in the first line.
The second (rather long) line will contain M numbers separated by spaces.
Answer should contain exactly N values, separated by spaces. First should give amount of 1-s, second - amount of 2-s and so on.
"""
input_data = input().split()

count = int(input_data[0])

upper_limit = int(input_data[1])

data_set = input().split()

data_set = [int(x) for x in data_set]

results = []

for i in range(upper_limit):
    results.append(0)

for i in data_set:
    results[i - 1] += 1

results = [str(x) for x in results]

print(' '.join(results))