#!/usr/bin/env python3
import math
import sys

cache_data = []
for line in sys.stdin:
    cache_data.append(line)

for line in cache_data:
    record = line.strip().split('\t')
    row_matrix1 = record[0]
    column_value_array_matrix1 = record[1].split(',')

    denominator1 = 0
    for column_value in column_value_array_matrix1:
        score = column_value.split('_')[1]
        denominator1 += pow(float(score), 2)
    denominator1 = math.sqrt(denominator1)
    # print(denominator1)

    for line in cache_data:
        record = line.strip().split('\t')
        row_matrix2 = record[0]
        column_value_array_matrix2 = record[1].split(',')

        denominator2 = 0
        for column_value in column_value_array_matrix2:
            score = column_value.split('_')[1]
            denominator2 += pow(float(score), 2)
        denominator2 = math.sqrt(denominator2)
        # print(denominator2)

        numerator = 0
        for column_value_matrix1 in column_value_array_matrix1:
            column_matrix1 = column_value_matrix1.split('_')[0]
            value_matrix1 = column_value_matrix1.split('_')[1]
            for column_value_matrix2 in column_value_array_matrix2:
                column_matrix2 = column_value_matrix2.split('_')[0]
                value_matrix2 = column_value_matrix2.split('_')[1]
                if column_matrix1 == column_matrix2:
                    numerator += int(value_matrix2) * int(value_matrix1)
        cos = numerator / (denominator1 * denominator2)
        if cos == 0:
            continue
        print("%s\t%s" % (str(row_matrix1), row_matrix2 + '_' + round(cos, 2)))
