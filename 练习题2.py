# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 10:36:55 2018

@author: 96122
"""

profit=int(input("Input profits:"))
if(profit<=100000):
    award=profit*0.1
elif(profit>100000 and profit<200000):
    award=10000+(profit-100000)*0.075
elif(profit>=200000 and profit<=400000):
    award=17500+(profit-200000)*0.05
elif(profit>400000 and profit<600000):
    award=27500+(profit-400000)*0.03
elif(profit>=600000 and profit<=1000000):
    award=33500+(profit-600000)*0.015
elif(profit>1000000):
    award=39500+(profit-1000000)*0.01
print("award is:",award)