# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:18:25 2020

@author: Khalil
"""
vide=""
i=0
ch=input("donner une chaine")

while len(ch)==0:
    print('donner une chaine non vide')
    ch=input("donner une chaine")
n= int(input("donner un entier"))
while n>len(ch)-1:
    print('Entier doit inf à len(ch)')
    n= int(input("donner un entier"))    
while i<n-1:
        
        vide=vide+ch[i]
        i=i+1
for i in range(n,len(ch)):
        vide=vide+ch[i]
print(vide)
