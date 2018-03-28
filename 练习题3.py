# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 10:52:19 2018

@author: 96122
"""
result=[]
flag=0
for i in range(2,85):
    j=168/i
    if(j%2==0 and i%2==0):
        n=(i-j)/2
        x=n*n-100
        for i in result:
            if i==x:
                flag=1
        if(flag==0):
            result.append(x)
print(result)
        