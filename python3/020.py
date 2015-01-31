"""
Vowel Count
Problem #20
http://www.codeabbey.com/index/task_view/vowel-count

This is a simple problem to get introduced to string processing. You will be given several lines of text - and for each of them you should tell the number of vowels (i.e. letters a, o, u, i, e, y). Note: that y is regarded as vowel for purpose of this task.

Though simple, this technic is important in cipher-breaking approaches. For example refer to Caesar Cipher Cracker problem.

Input data contain number of test-cases in the first line.
Then the specified number of lines follows each representing one test-case.
Lines consist only of lowercase English (Latin) letters and spaces.
Answer should contain the number of vowels in each line, separated by spaces.
"""
count = int(input())

results = []

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

for i in range(count):
    line = input()
    vowel_count = 0
    for l in line:
        if l in vowels:
            vowel_count += 1
    results.append(str(vowel_count))

print(' '.join(results))