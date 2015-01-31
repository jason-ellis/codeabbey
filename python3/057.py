"""
Smoothing the Weather
Problem #57
http://www.codeabbey.com/index/task_view/smoothing-the-weather

Little Merlin wants to become a meteorologist. He measures the temperature of the air each hour so that after several days he has a long sequence of values.

However, his instruments are not ideal so the measurements are not exact - they randomly jump up and down by several degrees from the real values.

Observing this, Merlin decided to make his data more smooth. To achieve this he only needs every value to be substituted by the average of it and its two neighbors. For example, if he have the sequence of 5 values like this:

3 5 6 4 5
Then the second (i.e. 5) should be substituted by (3 + 5 + 6) / 3 = 4.66666666667,
the third (i.e. 6) should be substituted by (5 + 6 + 4) / 3 = 5,
the fourth (i.e. 4) should be substituted by (6 + 4 + 5) / 3 = 5.
By agreement, the first and the last values will remain unchanged.

At the picture above the blue line shows unprocessed data while red represents the smoothing.

You are to write the program which helps Little Merlin in this whimsical algorithm of digital signal processing.

Input data will contain the length of the sequence in the first line.
The second line will contain the measurements itself.
Answer should contain the processed sequence. All values should be calculated to precision of 1e-7 or better.
"""
count = int(input())

nums = input().split()

nums = [float(x) for x in nums]

smoothed = []

for k,v in enumerate(nums):
    if k is 0 or k is len(nums)-1:
        smoothed.append(v)
    else:
        a = v
        b = nums[k-1]
        c = nums[k+1]
        smoothed.append((a + b + c)/3)

smoothed = [str(x) for x in smoothed]

print(' '.join(smoothed))