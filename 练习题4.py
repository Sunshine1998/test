# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:01:03 2018

@author: 96122
"""

from sklearn import svm

#准备训练样本
x=[[0,0],[1,1],[1,0]]
y=[0,1,1]

clf=svm.SVC()  
clf.fit(x,y)
print("预测[2,2]为：",clf.predict([[2,2]]))