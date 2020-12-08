import numpy as np

mat = np.zeros([64460, 9890], dtype=np.float)

with open('./recommender/output_5.txt', 'r') as f:
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
        itemSetT[itemMatIndex] = itemid
        itemMatIndex += 1
    ds = ds.split(',')
    for d in ds:
        if len(d.split('_')) < 2:
            continue
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

input_itemId = int(input('Please input id of the item(e.g.1000042): '))
while input_itemId not in itemSet:
    print('not existed')
    input_itemId = int(input('Please input id of the item again(e.g.1000042): '))

selected_item = mat[itemSet[input_itemId]]
userStr = []
sorted_user = sorted(range(len(selected_item)), key=lambda k: selected_item[k], reverse=True)
none_zero = np.count_nonzero(sorted_user)
if none_zero > 5:
    for user in sorted_user[:5]:
        value = selected_item[user]
        print("Recommend to user %s, rate %.2f"%(str(userSetT[user]),value))
        # userStr.append('{}_{:.2f}'.format(userSetT[user], value))
    # print(userStr)
else:
    for user in sorted_user:
        value = selected_item[user]
        if value > 0:
            print("Recommend to user %s, rate %.2f" % (str(userSetT[user]), value))
            # userStr.append('{}_{:.2f}'.format(userSetT[user], value))
    # print(userStr)
