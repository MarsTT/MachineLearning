#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X = []
f = open("city.txt")
#从文件读取经纬度
for v in f:
    #print v
    X.append([float(v.split('\t')[3]),float(v.split('\t')[4])])
    #print X
#转换成numpy array
X = np.array(X)
#设置类簇的数量
n_cluster = 5
#把数据和对应的分类数放入聚类函数中进行聚类
cls = KMeans(n_cluster).fit(X)
#X中没想所属分类的一个列表
cls.labels_


#画图
markers = ['^','x','o','*','+']
for i in range(n_cluster):
    members = cls.labels_ == i
    plt.scatter(X[members,0],X[members,1],s=60,marker=markers[i],c='b',alpha=0.5)

plt.title('')
plt.show()

