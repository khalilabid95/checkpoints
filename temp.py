# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
#begin1
import math
Mylist=[]
for x in range(2000,3201):
    if math.fmod(x,7)==0 and math.fmod(x,5)!=0:
        Mylist.append(x)
print (Mylist)
#end1      