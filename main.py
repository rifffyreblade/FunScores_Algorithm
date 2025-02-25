# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes,  files,  tool windows,  actions,  and settings.
import array as arr
import itertools
import time
from collections import OrderedDict
import gc

import numpy as np
import array

from itertools import permutations
from itertools import combinations
from itertools import product

P = (6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6)
S = (6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6)
B = (6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6)
M = (6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6)
K = (6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6)
L = (6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6)
# PS = [1, 1, 0, 0, 0, 0]
# PB = [1, 0, 1, 0, 0, 0]
# PM = [1, 0, 0, 1, 0, 0]
# PK = [1, 0, 0, 0, 1, 0]
# PL = [1, 0, 0, 0, 0, 1]
# SB = [0, 1, 1, 0, 0, 0]
# SM = [0, 1, 0, 1, 0, 0]
# SK = [0, 1, 0, 0, 1, 0]
# SL = [0, 1, 0, 0, 0, 1]
# BM = [0, 0, 1, 1, 0, 0]
# BK = [0, 0, 1, 0, 1, 0]
# BL = [0, 0, 1, 0, 0, 1]
# MK = [0, 0, 0, 1, 1, 0]
# ML = [0, 0, 0, 1, 0, 1]
# SL = [0, 0, 0, 0, 1, 1]
#
# ZeroPS = [0, 0, 0, 0, 0, 0]
# ZeroPB = [0, 0, 0, 0, 0, 0]
# ZeroPM = [0, 0, 0, 0, 0, 0]
# ZeroPK = [0, 0, 0, 0, 0, 0]
# ZeroPL = [0, 0, 0, 0, 0, 0]
# ZeroSB = [0, 0, 0, 0, 0, 0]
# ZeroSM = [0, 0, 0, 0, 0, 0]
# ZeroSK = [0, 0, 0, 0, 0, 0]
# ZeroSL = [0, 0, 0, 0, 0, 0]
# ZeroBM = [0, 0, 0, 0, 0, 0]
# ZeroBK = [0, 0, 0, 0, 0, 0]
# ZeroBL = [0, 0, 0, 0, 0, 0]
# ZeroMK = [0, 0, 0, 0, 0, 0]
# ZeroML = [0, 0, 0, 0, 0, 0]
# ZeroSL = [0, 0, 0, 0, 0, 0]
#
# minusPS = [-1, -1, 0, 0, 0, 0]
# minusPB = [-1, 0, -1, 0, 0, 0]
# minusPM = [-1, 0, 0, -1, 0, 0]
# minusPK = [-1, 0, 0, 0, -1, 0]
# minusPL = [-1, 0, 0, 0, 0, -1]
# minusSB = [0, -1, -1, 0, 0, 0]
# minusSM = [0, -1, 0, -1, 0, 0]
# minusSK = [0, -1, 0, 0, -1, 0]
# minusSL = [0, -1, 0, 0, 0, -1]
# minusBM = [0, 0, -1, -1, 0, 0]
# minusBK = [0, 0, -1, 0, -1, 0]
# minusBL = [0, 0, -1, 0, 0, -1]
# minusMK = [0, 0, 0, -1, -1, 0]
# minusML = [0, 0, 0, -1, 0, -1]
# minusSL = [0, 0, 0, 0, -1, -1]
#
# P = [1, 0, 0, 0, 0, 0]
# S = [0, 1, 0, 0, 0, 0]
# B = [0, 0, 1, 0, 0, 0]
# M = [0, 0, 0, 1, 0, 0]
# K = [0, 0, 0, 0, 1, 0]
# L = [0, 0, 0, 0, 0, 1]
#
# minusP = [-1, 0, 0, 0, 0, 0]
# minusS = [0, -1, 0, 0, 0, 0]
# minusB = [0, 0, -1, 0, 0, 0]
# minusM = [0, 0, 0, -1, 0, 0]
# minusK = [0, 0, 0, 0, -1, 0]
# minusL = [0, 0, 0, 0, 0, -1]
#
# arr.AddScore = [P, S, B, M, K, L]
# set1 = list(np.add(PB, minusML))
# set2 = list(np.add(PB, minusSK))
# set3 = list(np.add(SK, minusPB))
# set4 = list(np.add(SK, minusML))
# set5 = list(np.add(ML, minusPB))
# set6 = list(np.add(ML, minusSK))
# Question1 = [set1, set2, set3, set4, set5, set6]
# arr.SubScore = [minusP, minusS, minusB, minusM, minusK, minusL]
# bonusList = list(itertools.product(*(arr.AddScore, Question1, Question1, Question1, Question1, Question1, arr.SubScore)))
# print(bonusList[0])
# res = [i for n, i in enumerate(bonusList) if i not in bonusList[:n]]
# print(len(res))


i = 0
j = 0
start = time.time()

arr.setA1 = [P, S, B, M, K, L]
listOld = list(set(itertools.product(*arr.setA1)))
print(len(listOld))
print("--- %s seconds ---" % (time.time() - start))

arr.newArr = listOld
print(len(arr.newArr))
output = []
while i < len(arr.newArr):
    val = np.sum(arr.newArr[i])
    arr.Temp = arr.newArr[i]
    absVal = abs(arr.Temp[0]) + abs(arr.Temp[1]) + abs(arr.Temp[2]) + abs(arr.Temp[3]) + abs(arr.Temp[4]) + abs(
        arr.Temp[5])
    if val == 0:
        if absVal <= 14:
            output.append(arr.newArr[i])
    i = i + 1
i = 0
print(len(output))
Dexterity = []
BadDexterity = []
Strength = []
Courage = []
Precision = []
Grip = []
Endurance = []
Detection = []
Accuracy = []
Wit = []
Will = []
Mastery = []
Balance = []
Logic = []
Memory = []
Fortune = []
Power = []
BadPower = []
Speed = []
Body = []
Mind = []
Skill = []
Luck = []
Other3 = []
Other4 = []
Other5 = []
Zero = []
count = 0
pos_6 = 0
pos_min6 = 0
pos_dos6 = 0
pos_0 = 0
pos_0_array = []
pos_1 = 0
pos_1_array = []
pos_2 = 0
pos_2_array = []
pos_3 = 0
pos_3_array = []
pos_4 = 0
pos_4_array = []
pos_5 = 0
pos_5_array = []
pos_empty_array = []
while i < len(output):
    val = output[i]
    pos = 0
    neg = 0
    num6 = 0
    num_min6 = 0
    if val[0] >= 1:
        if val[0] < 6:
            pos += 1
        else:
            if val.count(-6) == 0:
                pos_6 += 1
                num6 += 1
    if val[0] <= -1:
        if val[0] > -6:
            neg += 1
        else:
            if val.count(6) == 0:
                pos_min6 += 1
                num_min6 += 1
    if val[1] >= 1:
        if val[0] < 6:
            pos += 1
        else:
            if val.count(-6) == 0:
                pos_6 += 1
                num6 += 1
    if val[1] <= -1:
        if val[0] > -6:
            neg += 1
        else:
            if val.count(6) == 0:
                pos_min6 += 1
                num_min6 += 1
    if val[2] >= 1:
        if val[0] < 6:
            pos += 1
        else:
            if val.count(-6) == 0:
                pos_6 += 1
                num6 += 1
    if val[2] <= -1:
        if val[0] > -6:
            neg += 1
        else:
            if val.count(6) == 0:
                pos_min6 += 1
                num_min6 += 1
    if val[3] >= 1:
        if val[0] < 6:
            pos += 1
        else:
            if val.count(-6) == 0:
                pos_6 += 1
                num6 += 1
    if val[3] <= -1:
        if val[0] > -6:
            neg += 1
        else:
            if val.count(6) == 0:
                pos_min6 += 1
                num_min6 += 1
    if val[4] >= 1:
        if val[0] < 6:
            pos += 1
        else:
            if val.count(-6) == 0:
                pos_6 += 1
                num6 += 1
    if val[4] <= -1:
        if val[0] > -6:
            neg += 1
        else:
            if val.count(6) == 0:
                pos_min6 += 1
                num_min6 += 1
    if val[5] >= 1:
        if val[0] < 6:
            pos += 1
        else:
            if val.count(-6) == 0:
                pos_6 += 1
                num6 += 1
    if val[5] <= -1:
        if val[0] > -6:
            neg += 1
        else:
            if val.count(6) == 0:
                pos_min6 += 1
                num_min6 += 1
    if num6 == 1:
        if num_min6 == 1:
            pos_6 = pos_6 - 1
            pos_min6 = pos_min6 - 1
            pos_dos6 += 1
            pos = 0
            neg = 0
    if pos == neg:
        pos_0 += 1
        pos_0_array.append(val)
    else:
        if pos == 1:
            if val.count(-5) == 1:
                if val.count(6) == 1:
                    pos_dos6 += 1
            if val.count(-6) == 1:
                if val.count(5) == 1:
                    pos_dos6 += 1
            else:
                pos_1 += 1
                pos_1_array.append(val)
        if pos == 2:
            if val.count(-5) == 1:
                if val.count(6) == 1:
                    pos_dos6 += 1
            if val.count(-6) == 1:
                if val.count(5) == 1:
                    pos_dos6 += 1
            else:
                pos_2 += 1
                pos_2_array.append(val)
        if pos == 3:
            if val.count(-5) == 1:
                if val.count(6) == 1:
                    pos_dos6 += 1
            if val.count(-6) == 1:
                if val.count(5) == 1:
                    pos_dos6 += 1
            else:
                pos_3 += 1
                pos_3_array.append(val)
        if pos == 4:
            if val.count(-5) == 1:
                if val.count(6) == 1:
                    pos_dos6 += 1
            if val.count(-6) == 1:
                if val.count(5) == 1:
                    pos_dos6 += 1
            else:
                pos_4 += 1
                pos_4_array.append(val)
        if pos == 5:
            if val.count(-5) == 1:
                if val.count(6) == 1:
                    pos_dos6 += 1
            if val.count(-6) == 1:
                if val.count(5) == 1:
                    pos_dos6 += 1
            else:
                pos_5 += 1
                pos_5_array.append(val)
        else:
            pos_empty_array.append(val)
            print(pos, neg)
    i += 1
print("Positive One: " + str(pos_1))
print(pos_1_array[0])
print("Positive Two: " + str(pos_2))
print(pos_2_array[0])
print("Positive Three: " + str(pos_3))
print(pos_3_array[0])
print("Positive Four: " + str(pos_4))
print(pos_4_array[0])
print("Positive Five: " + str(pos_5))
print(pos_5_array[0])
print("Score of 6: " + str(pos_6))
print("Score of -6: " + str(pos_min6))
print("Two Score of 6: " + str(pos_dos6))
print("Equals Zero: " + str(pos_0))
print(pos_0_array[0])
print(len(pos_empty_array))
print(pos_empty_array[0])
print("complete")
