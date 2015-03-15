"""
Rotate String
Problem #31
http://www.codeabbey.com/index/task_view/rotate-string

To rotate string by K characters means to cut these characters from the beginning and transfer them to the end. If K is negative, characters, on contrary should be transferred from the end to the beginning.

Input data will contain the number of test-cases in the first line.
Following lines will contain number K and some string S separated by space - one pair in each line.
String S will contain only small latin letters. K will not exceed half the length of S by absolute value.
Answer should contain strings rotated in accordance with the rule above, separated by spaces. For example:
"""
count = int(input())

results = []

for i in range(count):
    line = input().split()
    move_num = int(line[0])
    input_string = line[1]
    if move_num > 0:
        temp_string = input_string[:move_num]
        output_string = input_string.lstrip(temp_string)
        output_string = ''.join((output_string, temp_string))
    else:
        temp_string = input_string[move_num:]
        output_string = input_string.rstrip(temp_string)
        output_string = ''.join((temp_string, output_string))
    results.append(output_string)

print(' '.join(results))