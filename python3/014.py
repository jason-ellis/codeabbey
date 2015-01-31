"""
Modular Calculator
Problem #14
http://www.codeabbey.com/index/task_view/modular-calculator

This task provides practice for core property of remainder taking operation in arithmetic - persisting of the remainder over addition and multiplication. This important property is often used for checking results of calculations, in competitive programming, in calculation checksums and especially for encryption.
See Modular arithmetic for thorough explanations.

A kind of long arithmetic calculation is given to you and the answer should contain the result modulo some number.

If you are curious why modular arithmetic is that important, you can see Public Key Cryptography Intro and RSA Cryptography exercises.

Input data will have:

initial integer number in the first line;
one or more lines describing operations, in form sign value where sign is either + or * and value is an integer;
last line in the same form, but with sign % instead and number by which the result should be divided to get the remainder.
Answer should give remainder of the result of all operations applied sequentially (starting with initial number) divided by the last number.
"""
sum = int(input())

while True:
    try:
        data = input().split()
        if data[0] is '+':
            sum += int(data[1])
        elif data[0] is '*':
            sum *= int(data[1])
        elif data[0] is '%':
            print(sum % int(data[1]))
    except EOFError:
        break