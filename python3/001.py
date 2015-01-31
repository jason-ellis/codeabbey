"""
Sum "A+B"
Problem #1
http://www.codeabbey.com/index/task_view/sum-of-two

Since starting could be hard sometimes, let us try the simplest possible problem for practice on submitting answers etc.

You are to add two numbers and tell their sum. Though you can do it manually, try to write a simple program in any programming language you know or like or want to learn.

"""

numbers = input().split()
numbers = [int(x) for x in numbers]
print(numbers[0] + numbers[1])