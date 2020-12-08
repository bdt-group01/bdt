#!/usr/bin/env python
import sys

# input : "item1,item2,...,itemi+1"
# output: "count,item1,item2,...,itemi+1"

def readOneItemIndex(oneItemFile):
    oneItemDict = {}
    with open(oneItemFile, 'r') as f:
        oneItems = f.readlines()
    for oneItem in oneItems:
        oneItem = oneItem.strip().split(':')
        item = int(oneItem[1])
        indexs = oneItem[2].strip().split(',')
        indexs = [int(index) for index in indexs]
        oneItemDict[item] = set(indexs)
    return oneItemDict


def countInDat(itemset, oneItemDict):
    '''
    :param itemset: set
    :param datData: dict(item:indexs)
    :return:
    '''
    item = itemset[0]
    interSection = oneItemDict[item]
    for i in range(1, len(itemset)):
        interSection = set.intersection(interSection, oneItemDict[itemset[i]])

    return len(list(interSection))

def readLine(line):
    numbers = line.strip().split(',')
    data = [int(number) for number in numbers]
    return data

oneItemFile = sys.argv[1]

oneItemDict = readOneItemIndex(oneItemFile)

for i, line in enumerate(sys.stdin):
    lineData = readLine(line)
    count = countInDat(lineData, oneItemDict)
    lineDataStr = [str(item) for item in lineData]
    info = ','.join(lineDataStr)
    print('{},{}'.format(count, info))

