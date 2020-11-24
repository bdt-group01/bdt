#!/usr/bin/env python3

import sys

items = {}
result = {}


def update_item(items, user, score):
    if items.get(user) is None:
        items.setdefault(user, score)
    else:
        tmp = items[user]
        items.update({user: tmp + score})


for data in sys.stdin:
    data = data.strip()
    record = data.split('\t')
    item = record[0]
    user = record[1]
    score = record[2]
    if result.get(item) is None:
        items = {}
        update_item(items, user, score)
        result.setdefault(item, items)
    else:
        update_item(items, user, score)
        result[item] = items

for r in result:
    tmp = ''
    for u in result[r]:
        tmp += str(u) + '_' + str(result[r][u]) + ','
    print("%d\t%s" % (r, tmp[:-1]))
