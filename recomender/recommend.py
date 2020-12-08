import numpy as np
import argparse

parser = argparse.ArgumentParser(description='recommend the item to the user')
parser.add_argument('--input', '-input', help='the file name', type=str, required=True)
parser.add_argument('--number', '-n', help='the minmum number of user rate the item', type=int, required=True)
parser.add_argument('--rate', '-r', help='the data dimension', type=float, required=True)
parser.add_argument('--average', '-ave', help='whether The single rate is more than the input rate ', type=bool, required=False,default=False)

args = parser.parse_args()

file = args.input
n = args.number
r = args.rate
a = args.average


with open(file, 'r') as f:
    print("Begin recommend!")
    print("The minimum number of rate people is {}".format(n))
    print("The minimum rate is {}".format(r))
    datas = f.readlines()
    sum = 0
    for i, line in enumerate(datas):
        itemId, ds = line.split('\t')
        itemId = int(itemId)
        ds = ds.split(',')
        count = 0
        scores = 0
        ave = 0
        for d in ds:
            if len(d.split('_')) < 2:
                continue
            userId, score = d.split('_')
            score =  np.float32(score)
            if a == True and score < r:
                break
            scores += score
            count+=1
        if count > 0:
            ave = scores/count
        if ave > r and  count > n:
            print('{} {}'.format(itemId, ave))
            sum+=1
    print("There are {} items".format(sum))
    print("The recommend finished!")




