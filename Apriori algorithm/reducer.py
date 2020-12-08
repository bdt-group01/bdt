#!/usr/bin/env python
import sys
from itertools import combinations


s = 20

# input : "count,item1,item2,...,itemi"
# output: "item1,item2,...,itemi+1"

def readLine(line):
    numbers = line.strip().split(',')
    lineData = [int(number) for number in numbers]
    count = lineData[0]
    data = lineData[1:]
    return count, data

def constructCandidateItemsets(Li):
    '''
    :param Li: list(set)
    :return:
    '''
    candidateItemsets = []
    haveAddCandidateItemsetsDict = dict()
    for i in range(len(Li)):
        for j in range(i, len(Li)):
            candidateItemset = set.union(Li[i], Li[j])
            if len(candidateItemset) == len(Li[i]) + 1:
                candidateItemsetInfo = list(candidateItemset)
                candidateItemsetInfo.sort()
                candidateItemsetInfo = [str(itemInfo) for itemInfo in candidateItemsetInfo]
                candidateItemsetInfo = ','.join(candidateItemsetInfo)
                if candidateItemsetInfo in haveAddCandidateItemsetsDict.keys():
                    continue
                else:
                    haveAddCandidateItemsetsDict[candidateItemsetInfo] = True
                    candidateItemsets.append(candidateItemset)
    return candidateItemsets

# def constructCandidateItemsetsC(Li):
#     Li_flatten = list(set(item for items in Li for item in items))
#     new_N = len(Li[0]) + 1
#     condidateItemsets = list(combinations(Li_flatten, new_N))
#     return condidateItemsets



Li = []
for line in sys.stdin:
    count, data = readLine(line)
    if count > s:
        Li.append(set(data)) # for set merge
        # info = '{}'.format(data) # for sub Q1
        # print(info) # for sub Q1


candidateItemsets = constructCandidateItemsets(Li)
for itemset in candidateItemsets:
    itemsetsStr = [str(item) for item in itemset]
    itemsetsStr = ','.join(itemsetsStr)
    info = '{}'.format(itemsetsStr)
    print(info)
