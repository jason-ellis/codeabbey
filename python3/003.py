"""
Sums in Loop
Problem #3
http://www.codeabbey.com/index/task_view/sums-in-loop

If you already learned how to write program with a simple loop from Sum in Loop task, this new problem will be just a simple modification.

Now you will be given several pairs of values and you need to calculate sum for each pair.

Input data will contain the total count of pairs to process in the first line.
The following lines will contain pairs themselves - one pair at each line.
Answer should contain the results separated by spaces.

"""
count = int(input())

sums = []

for i in range(count):
    line = input().split()
    sum = 0
    for num in line:
        sum += int(num)
    sums.append(str(sum))

print(' '.join(sums))