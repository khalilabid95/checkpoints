# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:56:41 2020

@author: Khalil
"""
import math
mylist=[]
n= int(input('donner la taille de list'))
for i in range(0,n):
     x= int(input('donner un entier'))
     mylist.append(math.factorial(x))
print(mylist)