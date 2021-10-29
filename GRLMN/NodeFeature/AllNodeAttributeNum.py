from numpy import *
import numpy as np
import random
import math
import os
import time
import pandas as pd
import csv
import math
import random
import copy

# 定义函数
def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:  # 把每个rna疾病对加入OriginalData，注意表头
        SaveList.append(row)
    return

def ReadMyCsv2(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        counter = 0
        while counter < len(row):
            row[counter] = int(row[counter])      # 转换数据类型
            counter = counter + 1
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return


AllNode = []
ReadMyCsv(AllNode, 'AllNode.csv')

FinalLncFeature = []
ReadMyCsv(FinalLncFeature, 'FinalDrugFeature.csv')         # 部分由Gaussian部分生成

FinalMiFeature = []
ReadMyCsv(FinalMiFeature, 'FinalDiseaseFeature.csv')

FinalLncFeatureNum = []
counter = 0
while counter < len(FinalLncFeature):
    counter1 = 0
    while counter1 < len(AllNode):
        if FinalLncFeature[counter][0] == AllNode[counter1][0]:
            pair = []
            pair.append(str(counter1))
            pair.extend(FinalLncFeature[counter][1:])
            FinalLncFeatureNum.append(pair)
            break
        counter1 = counter1 + 1
    print(counter)
    counter = counter + 1

StorFile(FinalLncFeatureNum, 'FinalDrugFeatureNum.csv')


FinalMiFeatureNum = []
counter = 0
while counter < len(FinalMiFeature):
    counter1 = 0
    while counter1 < len(AllNode):
        if FinalMiFeature[counter][0] == AllNode[counter1][0]:
            pair = []
            pair.append(str(counter1))
            pair.extend(FinalMiFeature[counter][1:])
            FinalMiFeatureNum.append(pair)
            break
        counter1 = counter1 + 1
    print(counter)
    counter = counter + 1

StorFile(FinalMiFeatureNum, 'FinalDiseaseFeatureNum.csv')
