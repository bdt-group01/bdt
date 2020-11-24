#!/usr/bin/env python3

import sys

last_row = -1
res = []
tmp = ''
for data in sys.stdin:
    record = data.strip().split('\t')
    row = record[0]
    value = record[1]
    if last_row != -1 and row != last_row:
        print("%s\t%s" % (last_row, tmp[:-1]))
        tmp = value + ','
    else:
        tmp += value + ','
    last_row = row
print("%s\t%s" % (last_row, tmp[:-1]))
