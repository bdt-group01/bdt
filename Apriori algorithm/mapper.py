#!/usr/bin/env python
import sys

# input : "count,item1,item2,...,itemi"
# output: "count,item1,item2,...,itemi"


def readLine(line):
    numbers = line.strip().split(',')
    lineData = [int(number) for number in numbers]
    count = lineData[0]
    data = lineData[1:]
    return count, data

for line in sys.stdin:
    count, data = readLine(line)
    lineDataStr = [str(item) for item in data]
    info = ','.join(lineDataStr)
    print('{},{}'.format(count, info))

