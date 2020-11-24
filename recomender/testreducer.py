#!/usr/bin/env python3
import math


# def update_item(items, user, score):
#     if items.get(user) is None:
#         items.setdefault(user, score)
#     else:
#         tmp = items[user]
#         items.update({user: tmp + score})
#
#
# items = {}
# result = {}
# test = [
#     '1\t1_2,3_5',
#     '2\t1_10,2_3',
#     '3\t3_15',
#     '4\t1_3,3_5',
#     '5\t2_3',
#     '6\t1_5,2_5',
# ]

test = [
    '1\t1_1.0',
    '1\t2_0.36',
    '1\t3_0.93',
    '1\t4_0.93',
    '1\t6_0.26',
    '2\t1_0.36',
    '2\t2_1.0',
    '2\t4_0.49',
    '2\t5_0.29',
    '2\t6_0.88',
    '3\t1_0.93',
    '3\t3_1.0',
    '3\t4_0.86',
    '4\t1_0.99',
    '4\t2_0.49',
    '4\t3_0.86',
    '4\t4_1.0',
    '4\t6_0.36',
    '5\t2_0.29',
    '5\t5_1.0',
    '5\t6_0.71',
    '6\t1_0.26',
    '6\t2_0.88',
    '6\t4_0.36',
    '6\t5_0.71',
    '6\t6_1.0',
]

last_row = -1
res = []
tmp = ''
for line in test:
    record = line.strip().split('\t')
    row = record[0]
    value = record[1]
    if last_row != -1 and row != last_row:
        # res.append(tmp)
        print("%s\t%s" % (last_row, tmp[:-1]))
        tmp = value + ','
    else:
        tmp += value + ','
    last_row = row
print("%s\t%s" % (last_row, tmp[:-1]))


# cache_data = []
# for line in test:
#     cache_data.append(line)
#
# for line in cache_data:
#     record = line.strip().split('\t')
#     row_matrix1 = record[0]
#     column_value_array_matrix1 = record[1].split(',')
#
#     denominator1 = 0
#     for column_value in column_value_array_matrix1:
#         score = column_value.split('_')[1]
#         denominator1 += pow(float(score), 2)
#     denominator1 = math.sqrt(denominator1)
#     # print(denominator1)
#
#     for line in cache_data:
#         record = line.strip().split('\t')
#         row_matrix2 = record[0]
#         column_value_array_matrix2 = record[1].split(',')
#
#         denominator2 = 0
#         for column_value in column_value_array_matrix2:
#             score = column_value.split('_')[1]
#             denominator2 += pow(float(score), 2)
#         denominator2 = math.sqrt(denominator2)
#         # print(denominator2)
#
#         numerator = 0
#         for column_value_matrix1 in column_value_array_matrix1:
#             column_matrix1 = column_value_matrix1.split('_')[0]
#             value_matrix1 = column_value_matrix1.split('_')[1]
#             for column_value_matrix2 in column_value_array_matrix2:
#                 column_matrix2 = column_value_matrix2.split('_')[0]
#                 value_matrix2 = column_value_matrix2.split('_')[1]
#                 if column_matrix1 == column_matrix2:
#                     numerator += int(value_matrix2) * int(value_matrix1)
#         cos = numerator / (denominator1 * denominator2)
#         if cos == 0:
#             continue
#         print("%s\t%s" % (str(row_matrix1), row_matrix2 + '_' + str(round(cos, 2))))

#     user = record[1]
#     score = record[2]
#     if result.get(item) is None:
#         items = {}
#         update_item(items, user, score)
#         result.setdefault(item, items)
#     else:
#         update_item(items, user, score)
#         result[item] = items
#
# for r in result:
#     tmp = ''
#     for u in result[r]:
#         tmp += str(u) + '_' + str(result[r][u]) + ','
#     print("%d,%s" % (r, tmp[:-1]))

# def update_item(items, user, score):
#     if items.get(user) is None:
#         items.setdefault(user, score)
#     else:
#         tmp = items[user]
#         items.update({user: tmp + score})
#
#
# items = {}
# result = {}
# test = [[1, 1, 1], [1, 1, 1], [1, 3, 5],
#         [2, 1, 10], [2, 2, 3],
#         [3, 3, 5], [3, 3, 10],
#         [4, 1, 3], [4, 3, 5],
#         [5, 2, 3],
#         [6, 1, 5], [6, 2, 5],
#         ]
# last_item = -1
# for record in test:
#     # data = data.strip()
#     # record = data.split('\t')
#     item = record[0]
#     user = record[1]
#     score = record[2]
#     if result.get(item) is None:
#         items = {}
#         update_item(items, user, score)
#         result.setdefault(item, items)
#     else:
#         update_item(items, user, score)
#         result[item] = items
#
# for r in result:
#     tmp = ''
#     for u in result[r]:
#         tmp += str(u) + '_' + str(result[r][u]) + ','
#     print("%d\t%s" % (r, tmp[:-1]))
