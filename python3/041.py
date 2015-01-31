"""
Median of Three
Problem #41
http://www.codeabbey.com/index/task_view/median-of-three

You probably already solved the problem Minimum of Three - and it was not great puzzle for you? Since programmers should improve their logic (and not only skills in programming language), let us change the task to make it more tricky.

You will be again given triplets of numbers, but now the middle of them should be chosen - i.e. not the largest and not the smallest one. Such number is called the Median (of the set, array etc).

Be sure, this problem is not simply "another stupid exercise" - it is used as a part in powerful QuickSort algorithm, for example.

Input data will contain in the first line the number of triplets to follow.
Next lines will contain one triplet each.
Answer should contain selected medians of triplets, separated by spaces.
"""
count = int(input())

results = []

for i in range(count):
    nums = input().split()
    nums = [int(x) for x in nums]
    nums.remove(min(nums))
    nums.remove(max(nums))
    results.append(str(nums[0]))

print(' '.join(results))