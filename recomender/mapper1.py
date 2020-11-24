#!/usr/bin/env python3

import sys

for line in sys.stdin:
    record = line.strip().split(',')
    user = record[0]
    item = record[1]
    behavior = record[2]
    if behavior == 'pv':
        behavior = 1
    elif behavior == 'cart':
        behavior = 3
    elif behavior == 'fav':
        behavior = 5
    elif behavior == 'buy':
        behavior = 10
    print('\t'.join([item, user, behavior]))
