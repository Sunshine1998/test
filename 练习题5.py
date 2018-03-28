# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:12:36 2018

@author: 96122
"""
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_table("C:/Users/96122/Desktop/basketball data.txt",encoding='utf-8')
x=df[['2']]
y=df[['6']]
print(x,y)
'''X=df['assists_per_minute','points_per_minute']
clf = KMeans(n_clusters=3)
y_pred = clf.fit_predict(X)
plt.scatter(x=df['assists_per_minute'], y=df['points_per_minute'], c=y_pred, marker='x')
plt.title("Kmeans-Basketball Data")
plt.xlabel("assists_per_minute")
plt.ylabel("points_per_minute")
plt.show()'''