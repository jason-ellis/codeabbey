"""
Reverse String
Problem #30
http://www.codeabbey.com/index/task_view/reverse-string

Quite a simple task - just to start learning strings...

Input data will contain a single string of small latin letters and few spaces.
Answer should contain the string of the same length with the same characters but in reverse order.
"""
words = input()

rev_words = []

rev_words = [x for x in words]

for i in range(len(rev_words)):
    print(rev_words.pop())