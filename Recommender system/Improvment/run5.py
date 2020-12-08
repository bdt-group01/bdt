import numpy as np
import minpy.numpy as mnp


mat = np.zeros([64460, 9890], dtype=np.float)

with open('../data/output_4.txt', 'r') as f:
    datas = f.readlines()

itemSet = {}
itemSetT = {}
userSet = {}
userSetT = {}
itemMatIndex = 0
userMatIndex = 0

for i, line in enumerate(datas):
    itemid, ds = line.split('\t')
    itemid = int(itemid)
    if itemid in itemSet.keys():
        None
    else:
        itemSet[itemid] = itemMatIndex
        itemSetT[itemMatIndex] =itemid
        itemMatIndex += 1
    ds = ds.split(',')
    for d in ds:
        userid, score = d.split('_')
        userid, score = int(userid), np.float32(score)
        if userid in userSet.keys():
            None
        else:
            userSet[userid] = userMatIndex
            userSetT[userMatIndex] = userid
            userMatIndex += 1

        matUserIndex, matItemIndex = userSet[userid], itemSet[itemid]
        mat[matItemIndex, matUserIndex] = score
    # print('{}/{}'.format(i, len(datas)))
print(mat[0:20,0:20])




mat2 = np.zeros([64460, 9890], dtype=np.float)

with open('../data/part-r-000001', 'r') as f:
    datas = f.readlines()

for i, line in enumerate(datas):
    itemid, ds = line.split('\t')
    itemid = int(itemid)
    if itemid not in itemSet.keys():
        continue

    ds = ds.split(',')
    for d in ds:
        userid, score = d.split('_')
        userid, score = int(userid), np.float32(score)
        if userid not in userSet.keys():
            continue
        else:
            matUserIndex = userSet[userid]
            matItemIndex = itemSet[itemid]
            mat2[matItemIndex, matUserIndex] = score

print(mat2.sum(axis=1))
print(mat2[0:100,0:100])
mat2[mat2>0] = -1
print(mat2[0:20,0:20])
mat2[mat2==0] = 1
print(mat2[0:20,0:20])
mat2[mat2==-1] = 0
print(mat2[0:20,0:20])


result = mnp.multiply(mat, mat2)
print(result[0:20, 0:20])


output = ''
for itemIndexId in range(64460):
    itemStr = '{}\t'.format(itemSetT[itemIndexId])
    userStr = []
    for userIndexId in range(980):
        value = result[itemIndexId, userIndexId]
        if value > 0:
            userStr.append('{}_{:.2f}'.format(userSetT[userIndexId], value))
    userStr = ','.join(userStr)
    itemStr = itemStr + userStr + '\n'
    output += itemStr
    if itemIndexId % 100 == 0:
        print('{}/{}'.format(itemIndexId, 64460))
    # break
# print(output)

with open('../data/output_5.txt', 'w') as fo:
    fo.write(output)


