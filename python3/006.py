"""
Rounding
Problem #6
http://www.codeabbey.com/index/task_view/rounding

When program deals with numbers which have fraction part we sometimes want to round such values to whole integer. We'll need this for programming some later problems (to make answers more uniform, for example), so let us have the following dedicated exercise to learn this trick.

There are several pairs of numbers. For each pair you are to divide first by second and return the result, rounded to nearest integer.

In cases, when result contains exactly 0.5 as a fraction part, value should be rounded up (i.e. to next integer greater than given one). Note that for negative values "greater" means "closer to zero". Refer to the Wikipedia page on Rounding for more thorough explanations.

In any further problems, when rounding is mentioned - just the same rounding algorithm is supposed (unless other is explicitly specified).
"""
count = int(input())

results = []

for i in range(count):
    a, b = input().split()
    a = int(a)
    b = int(b)

    num = float(a / b)
    rem = num % 1

    if rem >= .5:
        num = int(num - rem + 1)
    else:
        num = int(num - rem)
    results.append(str(num))

print(' '.join(results))