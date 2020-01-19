# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:38:22 2020

@author: Khalil
"""
import math




def indice(ch):
    k=0
    myindice=[-1]
    for i in range(0,len(ch)-1):
        
        if ch[i]==',':
           k=k+1
           myindice.append(i)
    print(myindice)
    print(k)
    return (myindice)


def transfert(ch,myindice):
    i=0
    mylist=[]
    mylist1['','','','']
    while i<len(ch)-1:
        for j in range(myindice[i]+1,myindice[i+1]):
            mylist1[i]=mylist1[i]+ch[j]
            b=float(mylist1[i])
        mylist.append(b)
        i=i+1
    print(mylist)
    return (mylist)
    
def fonction(d):
    c=50
    h=30
    q=round((math.sqrt(2*c*d/h)))
    print(q)
    return(q)
    
ch=input('donner une chaine' ) 
valeur=[] 
x=indice(ch)
y=transfert(ch,x)
for i in range(0,len(y)):
    valeur.append(fonction(y[i]))
print(valeur)
 


    
    
    
    
    
    
    
    
    
    
    
    
    
    






    