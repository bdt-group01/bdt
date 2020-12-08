#!/usr/bin/env python

import sys
import csv

# input comes from STDIN (standard input)

for line in sys.stdin:
    line = line.strip()
    for csv_line in csv.reader([line]):
        splits = csv_line
        #print(splits)
    if splits[3].strip() == 'buy':    # only get "buy" record
        print ('%s^%s' % (splits[0].strip(), splits[4].strip()))   # print userId and timestamp


