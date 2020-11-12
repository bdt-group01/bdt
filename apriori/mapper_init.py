#!/usr/bin/env python
import sys

saveFile = sys.argv[1]


def readLine(line):
    numbers = line.strip().split(' ')
    lineData = [int(number) for number in numbers]
    return lineData


currentItemsets = []
currentItemsetsCount = []
currentItemsetsDocumentIndex = []


for i, line in enumerate(sys.stdin):
    lineData = readLine(line)
    for d in lineData:
        if d in currentItemsets:
            index = currentItemsets.index(d)
            currentItemsetsCount[index] += 1
            currentItemsetsDocumentIndex[index].append(i)
        else:
            currentItemsets.append(d)
            currentItemsetsCount.append(1)
            currentItemsetsDocumentIndex.append([i])

f = open(saveFile, 'w')

for i in range(len(currentItemsets)):
    count, itemset, indexs = currentItemsetsCount[i], currentItemsets[i], currentItemsetsDocumentIndex[i]
    indexsStr = [str(index) for index in indexs]
    indexsStr = ','.join(indexsStr)
    info = '{},{}'.format(count, itemset)
    print(info)
    longInfo = '{}:{}:{}\n'.format(count, itemset, indexsStr)
    f.write(longInfo)

f.close()




