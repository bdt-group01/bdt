#!/usr/bin/env python

import sys
from datetime import datetime

currentUser = "-1"
frequency = 0
latest_timestamp = 0
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #print(line)
    # parse the input we got from a_mapper.py
    userId, timestamp = line.split("^")
    #print(currentUser, userId)
    if currentUser == "-1":
        currentUser = userId
        frequency += 1
        latest_timestamp = max(latest_timestamp, int(timestamp))
    elif currentUser == userId:
        frequency += 1
        latest_timestamp = max(latest_timestamp, int(timestamp))
    else:
        #print("~",currentUser, userId)
        date = '{:%m%d%H%M}'.format(datetime.fromtimestamp(latest_timestamp))
        print('%s,%s' % (latest_timestamp, frequency))
        currentUser = userId
        frequency = 1
        latest_timestamp = int(timestamp)
date = '{:%m%d%H%M}'.format(datetime.fromtimestamp(latest_timestamp))
print('%s,%s' % (latest_timestamp, frequency))      # print users' latest purchase record and their purchase frequency for kmeans



