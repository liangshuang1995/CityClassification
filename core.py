# -*- coding:utf-8 -*-
"""
@version:
author:liangs1995
@time: 2020/07/22
@file: core.py
@function:
@modify:
"""

import pandas as pd
import numpy as np
import os
import datetime


# 城市分级特征
def cityClassification(tablePath):
    cityClaPath = "CityClassification.txt"
    if not os.path.exists(cityClaPath):
        print("error: no this txt")
    f = open(cityClaPath, 'r')
    lines = f.readlines()
    # 城市等级，新一线记为1.5，没有的记为6
    label = [1, 1.5, 2, 3, 4, 5]
    labelIndex = -1
    cityClaDict = dict()
    for line in lines:
        if "#" in line:
            labelIndex += 1
        else:
            line = line.replace('\n', '')
            subLine = line.split('|')
            tempDict = dict(zip(subLine, label[labelIndex]*np.ones(len(subLine))))
            cityClaDict.update(tempDict)

    f.close()
    cityClaData = []
    data = pd.read_csv(tablePath)
    for index, row in data.iterrows():
        tempCityClaData = 6
        city = row['city']
        for (key, value) in cityClaDict.items():
            if key in city:
                tempCityClaData = value
                break
        cityClaData.append(tempCityClaData)

    data['cityClassification'] = cityClaData
    print(data.shape)
    print(data.columns)
    data.to_csv("cityClassificationData.csv", index=False)


def main():
    startTime = datetime.datetime.now()
    pathTable1 = "testData.csv"
    cityClassification(pathTable1)
    endTime = datetime.datetime.now()
    print((endTime - startTime).seconds)


if __name__ == "__main__":
    main()

