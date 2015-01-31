"""
Dice Rolling
Problem #43
http://www.codeabbey.com/index/task_view/dice-rolling

When programming board or role-playing games, many novice programmers experience troubles in converting random values to specific dice points. The goal of this task is to give a practice in simulation of dice rolling by the values coming from a random numbers generator.

Suppose, we have generator which gives random values in range from 0 (inclusive) to 1 (not inclusive) - this could be encountered in languages like Basic, Java, Matlab etc.

We want to convert these values with floating point to one of six integer numbers: from 1 to 6. This could be achieved by the following steps:

Multiply random value by N which is the number of distinct values we want to get - in our case we multiply by 6 and so result would be floating point value in range from 0 (inclusive) to 6 (not inclusive)
Now let us take the integer part of this result (calling function like floor or converting to int) - the value will become one of 0, 1, 2, 3, 4, 5 with equal probability.
Since we need values from 1 to 6 let us simply add 1 to the result.
Now you'll be given several numbers in the range [0 .. 1) (be sure, they are provided by random number generator) - and you are to convert them to dice points by applying the algorithm above.

Input data will contain the amount of values to convert in the first line.
Other lines will contain one value each, in form like 0.142857.
Answer should contain numbers from 1 to 6 for each of input values, produced by the discussed algorithm.
"""
count = int(input())

results = []

for i in range(count):
    roll = float(input())
    roll *= 6
    roll += 1
    roll = int(roll)
    results.append(str(roll))

print(' '.join(results))