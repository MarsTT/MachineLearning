#coding=utf-8

from numpy import *

def loadDataset():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset,C1)

def scanD(D,Ck,min_sup):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                ssCnt[can] = ssCnt.get(can,0)+1
    numItems = float(len(D))
    retList = []
    supData = {}
    for key in ssCnt:
        sup = ssCnt[key] / numItems
        if sup >= min_sup:
            retList.insert(0,key)
        supData[key] = sup
    return retList,supData


def aprioriGen(Lk,k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1,lenLk):
            L1 = list(Lk[i])[:k-2]
            L2 = list(Lk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i]| Lk[j])
    return retList

def apriori(dataSet,min_sup=0.5):
    C1 = createC1(dataSet)
    D = map(set,dataSet)
    L1,supData = scanD(D,C1,min_sup)
    L = [L1]
    k = 2
    while(len(L[k-2]) > 0 ):
        Ck = aprioriGen(L[k-2],k)
        Lk,supK = scanD(D,Ck,min_sup)
        supData.update(supK)
        L.append(Lk)
        k += 1
    return L,supData