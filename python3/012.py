"""
Modulo and time difference
Problem #12
http://www.codeabbey.com/index/task_view/modulo-and-time-difference

Dealing with remainders may cause heavy headache to novice programmers. Let us write a simple program which has this operation for its core to study integer division better. At the same time we'll have some practice in handing dates - which sometimes gives headache even to experienced coders.

In arithmetic, the remainder (or modulus) is the amount "left over" after performing the division of two integers which do not divide evenly (from Wiki). This task will provide further practice with modulo operation.

Suppose, you are given two timestamps - for example, when the train or ferry boat starts its travel and when it finishes. This may look like:

start: May 3, 17:08:30
end  : May 8, 12:54:15
and you are curious to know, how much time (in days, hours, minutes and seconds) is spent in traveling (perhaps, to choose faster variant). How this could be achieved?

One of the easiest way is:

convert both timestamps to big numbers, representing seconds from the beginning of the month (or year, or century);
calculate their difference - i.e. travel time in seconds;
convert this difference back to days, hours, minutes and seconds.
First operation could be performed by multiplying minutes by 60 and hours by 60*60 etc. and summing all values up.
The third operation should be performed on contrary by several divisions with keeping remainders.

In this task you will be given several pair of timestamps. We suppose that both dates in the pair are always in the same month, so only number of day will be given. You are to calculate difference between timestamps in each pair.

Input data: the first line contains number of test-cases, other lines contain test-cases themselves.
Each test-case contains 8 numbers, 4 for each timestamp: day1 hour1 min1 sec1 day2 hour2 min2 sec2 (second timestamp will always be later than first).
Answer: for each test-case you are to output difference as following (days hours minutes seconds) - please note brackets - separated by spaces.
"""
count = int(input())

results = []

def big_date(d, h, m, s):
    s = s
    s += m*60
    s += h*60*60
    s += d*24*60*60
    return s

def format_date(s):
    s = s
    m = s / 60
    s %= 60
    h = m / 60
    m %= 60
    d = h / 24
    h %= 24
    return int(d), int(h), int(m), int(s)

for i in range(count):
    dates = input().split()
    #dates = ['1', '0', '0', '0', '2', '3', '4', '5']
    dates = [int(x) for x in dates]
    date1 = dates[:4]
    date2 = dates[4:]
    date1 = big_date(date1[0], date1[1], date1[2], date1[3])
    date2 = big_date(date2[0], date2[1], date2[2], date2[3])
    new_date = date2 - date1
    new_date = format_date(new_date)
    results.append(new_date)

results = ''.join(str(results))
print(results.replace(', ', ' ').replace('[', '').replace(']', ''))