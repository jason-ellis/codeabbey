"""
Palindromes
Problem #50
http://www.codeabbey.com/index/task_view/palindromes

The word or whole phrase which has the same sequence of letters in both directions is called a palindrome. Here are few examples:

Stats
Amore, Roma
No 'x' in Nixon
Was it a cat I saw?
As you see, case of the letters is ignored. Spaces and punctuations are ignored too.

Your goal in this programming exercise is to determine, whether the phrase represents a palindrome or not.

Input data contains number of phrases in the first line.
Next lines contain one phrase each.
Answer should have a single letter (space separated) for each phrase: Y if it is a palindrome and N if not.
"""
count = int(input())

for i in range(count):
    line = input()
    line = line.lower()
    line = line.replace('\n', '') \
        .replace(' ', '') \
        .replace(',', '') \
        .replace('.', '') \
        .replace('-', '') \
        .replace('?', '') \
        .replace('!', '')
    #print(line)
    if line == line[::-1]:
        print('Y ')
    else:
        print('N ')