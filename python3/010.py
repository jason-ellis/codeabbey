"""
Linear Function
Problem #10
http://www.codeabbey.com/index/task_view/linear-function

Very common problem in computational programming is to determine the underlying law to which some phenomenon obeys. For learning purpose let us practice a simple variant - discovering linear dependence by two given observations (for example, how the price for some product depends on its size, weight etc.)

Linear function is defined by an equation:

y(x) = ax + b
Where a and b are some constants.
For example, with a=3, b=2 function will yield values y = 2, 5, 8, 11...
for x = 0, 1, 2, 3...

Your task is to determine a and b by two points, belonging to the function.
I.e. you are told two pairs of values (x1, y1), (x2, y2) which satisfy the function equation - and you should restore the equation itself.

Input data have the number of test-cases in the first line
and then test-cases themselves in separate lines.
Each case contains 4 integers (x1 y1 x2 y2).
Answers should be integer too and you are to write them in line, separating with spaces and enclosing each pair in parenthesis, for example:
"""
count = int(input())

results = []

for i in range(count):
    x1, y1, x2, y2 = input().split()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    a = (y2 - y1) / (x2 - x1)
    b = y1 - (a*x1)
    results.append("({} {})".format(int(a), int(b)))

print(' '.join(results))