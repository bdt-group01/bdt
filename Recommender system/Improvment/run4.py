import numpy as np
import minpy.numpy as mnp

mat = np.zeros([64466, 64466], dtype=np.float16)
print(mat.shape)

with open('../data/part-r-000002', 'r') as f:
    datas = f.readlines()

indexSet = {}
indexSetT = {}
matIndex = 0
for i, line in enumerate(datas):
    index, ds = line.split('\t')
    index = int(index)
    if index in indexSet.keys():
        None
    else:
        indexSet[index] = matIndex
        indexSetT[matIndex] = index
        matIndex += 1
    ds = ds.split(',')
    for d in ds:
        index2, score = d.split('_')
        index2, score = int(index2), np.float32(score)
        if index2 in indexSet.keys():
            matIndex1, matIndex2 = indexSet[index], indexSet[index2]
            mat[matIndex1, matIndex2] =score
            mat[matIndex2, matIndex1] =score
        else:
            indexSet[index2] = matIndex
            indexSetT[matIndex] = index2
            matIndex1, matIndex2 = indexSet[index], indexSet[index2]
            mat[matIndex1, matIndex2] =score
            mat[matIndex2, matIndex1] =score
            matIndex += 1

print(len(indexSet.keys()))
print(matIndex)
print(mat.shape)
print(mat[0:50, 0:50])


mat2 = np.zeros([983, 64466], dtype=np.int)

with open('../data/part-r-000003', 'r') as f:
    datas = f.readlines()

userSet = {}
userSetT = {}
userMatIndex = 0

for i, line in enumerate(datas):
    userid, ds = line.split('\t')
    userid = int(userid)
    if userid in userSet.keys():
        None
    else:
        userSet[userid] = userMatIndex
        userSetT[userMatIndex] = userid
        userMatIndex += 1
    ds = ds.split(',')
    for d in ds:
        item, score = d.split('_')
        item, score = int(item), np.float32(score)
        matUserIndex, matItemIndex = userSet[userid], indexSet[item]
        mat2[matUserIndex, matItemIndex] = score
    # print('{}/{}'.format(i, len(datas)))
print(len(userSet.keys()))
print(userMatIndex)
print(mat2[0:50, 0:50])
mat2 = mat2.T

# result = mnp.dot(mat, mat2)


multiResult = mnp.zeros([64460, 980])
# multiResult = []

fold = 10

Dindex1 = 6446
Dindex2 = 98

for i in range(fold):
    # tempResult = []
    for j in range(fold):
        print(i,j)
        mat1Beg = i*Dindex1
        mat1End = (i+1)*Dindex1
        print('mat1:{}:{}'.format(mat1Beg, mat1End))
        mat2Beg = j*Dindex2
        mat2End = (j+1)*Dindex2
        print('mat2:{}:{}'.format(mat2Beg, mat2End))
        mat1part = mat[mat1Beg:mat1End, :]
        mat2part = mat2[:, mat2Beg:mat2End]
        partResult = mnp.dot(mat1part, mat2part)
        multiResult[mat1Beg:mat1End, mat2Beg:mat2End] = partResult

        print(type(partResult))
        # tempResult.append(partResult)
        print(partResult)
        print(partResult.shape)
    # multiResult.append(tempResult)

# multiResult = mnp.block(multiResult)
print(multiResult)
print(multiResult.shape)
print(mnp.sum(multiResult))
print(mnp.mean(multiResult))

        # multiResult[mat1Beg:mat1End, mat2Beg:mat2End] = partResult
    #
    #     if j == 9:
    #         mat1Beg = (i+1)*Dindex1
    #         mat1End = 64466
    #         print('mat1:{}:{}'.format(mat1Beg, mat1End))
    #         mat2Beg = j*Dindex2
    #         mat2End = (j+1)*Dindex2
    #         print('mat2:{}:{}'.format(mat2Beg, mat2End))
    #         mat1part = mat[mat1Beg:mat1End, :]
    #         mat2part = mat2[:, mat2Beg:mat2End]
    #         partResult = mnp.dot(mat1part, mat2part)
    #         multiResult[mat1Beg:mat1End, mat2Beg:mat2End] = partResult
    #
    # if i == 9:
    #     mat1Beg = (i+1)*Dindex1
    #     mat1End = 64466
    #     print('mat1:{}:{}'.format(mat1Beg, mat1End))
    #     mat2Beg = j*Dindex2
    #     mat2End = (j+1)*Dindex2
    #     print('mat2:{}:{}'.format(mat2Beg, mat2End))
    #     mat1part = mat[mat1Beg:mat1End, :]
    #     mat2part = mat2[:, mat2Beg:mat2End]
    #     partResult = mnp.dot(mat1part, mat2part)
    #     multiResult[mat1Beg:mat1End, mat2Beg:mat2End] = partResult

output = ''
for itemIndexId in range(64460):
    itemStr = '{}\t'.format(indexSetT[itemIndexId])
    userStr = []
    for userIndexId in range(980):
        value = multiResult[itemIndexId, userIndexId]
        if value > 0:
            userStr.append('{}_{:.2f}'.format(userSetT[userIndexId], value))
    userStr = ','.join(userStr)
    itemStr = itemStr + userStr + '\n'
    output += itemStr
    if itemIndexId % 100 == 0:
        print('{}/{}'.format(itemIndexId, 64460))
    # break
# print(output)

with open('../data/output.txt', 'w') as fo:
    fo.write(output)









