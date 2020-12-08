import os
import pandas as pd
import numpy

def getCategoryPerUser(data):
    outputData = []
    user = data['user']
    users = list(user.unique())
    for i, user in enumerate(users):
        tempdata = data[data['user']==user]
        category = tempdata['category'].unique()
        outputData.append(list(category))
        print('{}/{}'.format(i, len(users)))
    return outputData

def list2StrFile(categories, fileName):
    with open(fileName, 'w') as f:
        for category in categories:
            category = [str(_cate) for _cate in category]
            categoryStr = ' '.join(category)+'\n'
            f.write(categoryStr)


data = pd.read_csv('../../data/UserBehavior.csv')
categories = getCategoryPerUser(data)
list2StrFile(categories, './data.txt')

