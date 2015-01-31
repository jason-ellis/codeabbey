"""
Fahrenheit to Celsius
Problem #7
http://www.codeabbey.com/index/task_view/fahrenheit-celsius

This programming exercise is roughly the same as counting sums in loop, but it needs bit more calculations.

Note: the problem Rounding explains the rounding algorithm which is used in this task.

There are two widespread systems of measuring temperature - Celsius and Fahrenheit. First is quite popular in Europe and second is well in use in United States for example.

By Celsius scale water freezes at 0 degrees and boils at 100 degrees. By Fahrenheit water freezes at 32 degrees and boils at 212 degrees. You may learn more from wikipedia on Fahrenheit. Use these two points for conversion of other temperatures.

You are to write program to convert degrees of Fahrenheit to Celsius.

Input data contains N+1 values, first of them is N itself (Note that you should not try to convert it).
Answer should contain exactly N results, rounded to nearest integer and separated by spaces.
"""
data = input().split()

count = data.pop(0)

results = []

for fahrenheit in data:
    celsius = round((int(fahrenheit) - 32) * (5 / 9))
    results.append(str(celsius))

print(' '.join(results))