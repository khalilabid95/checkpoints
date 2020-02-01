# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:40:08 2020

@author: Khalil
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
file="C:\\Users\\Khalil\\Desktop\\formation\\train_and_test2.csv.csv"
nexdata=pd.read_csv(file, sep=',', encoding="ISO-8859-1")
nexdata.head(5)
#nexdata.isnull()
#plt.title('histogramme des ages')
#plt.xlabel('Age')
#nexdata['Age'].plot.hist()
#sns.distplot(nexdata['Age'],bins=10,hist=True,kde=True,color='red')
#nexdata['Age'].plot.box()
#nexdata['Sex'].plot.box()
#nexdata.plot.scatter(x="Age",y="Sex")
#sns.lmplot(x="Age",y="Sex",data=nexdata)
#sns.lmplot(x="Sex",y="2urvived",data=nexdata)
#sns.lmplot(x="Fare",y="2urvived",data=nexdata)

df=nexdata[['Passengerid','Age','Sex','Fare','sibsp','Parch','Pclass','2urvived','Embarked']]



def plot_correlation_map( df ):

    corr = df.corr()

    s , ax = plt.subplots( figsize =(12 , 10 ) )

    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )

    s = sns.heatmap(

        corr, 

        cmap = cmap,

        square=True, 

        cbar_kws={ 'shrink' : .9 }, 

        ax=ax, 

        annot = True, 

        annot_kws = { 'fontsize' : 12 }

        )
plot_correlation_map( df )
