# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:34:30 2019

@author: Haroon Traders
"""
'''names=['name','age','dept']'''
#data loading storage and file formats
import pandas as pd
#sentinels={'2':['not found','nan']}
#ab=pd.read_csv("C:/Users/Haroon Traders/source/repos/filing/filing/data.csv",skiprows=1,header=None,na_values=sentinels,nrows=3)
#print(ab)
#s2_df=pd.read_csv("C:/Users/Haroon Traders/source/repos/filing/filing/data.csv",index_col=['name','age'])
#print(s2_df),nrows=3,na_values=sentinels
#new=pd.read_csv("C:/Users/Haroon Traders/Anaconda3/pkgs/scikit-learn-0.20.3-py37h343c172_0/Lib/site-packages/sklearn/datasets/data/wine_data.csv",skiprows=1,header=None,chunksize=50)
#print(type(new))
#print(new)
#chunklist=[]
#for chunk in new:
#    print(len(chunk))  #178 record 3 chunks of 50 4th chunk will be of 28
    #print(chunk.head)
#   chunklist.append(chunk)
#print(chunklist)
#df=chunklist[2]
#print(df.head())
#print(df)
#ab=pd.read_csv("C:/Users/Haroon Traders/source/repos/filing/filing/data.csv",skiprows=1,header=None,na_values=sentinels,nrows=3)
#ab.to_csv("C:/Users/Haroon Traders/Anaconda3/pkgs/scikit-learn-0.20.3-py37h343c172_0/Lib/site-packages/sklearn/datasets/data/wine_data.csv")
#abc=pd.read_html("C:/Users\Haroon Traders/Downloads/[FreeTutorials.Us] Udemy - the-complete-web-developer-course-2/04 Javascript/108 Loops - Files.html")
#print(len(abc))
import numpy as np
'''
frame=pd.DataFrame({'a':np.random.randn(100),'b':np.random.randn(100)})
store=pd.HDFStore("mydata.h5")
#print(store)
#print(frame)
store['obj1']=frame
store['obj1_col']=frame['a']
print(store)
x=store.obj1
print(x.head())
#print(x)
y=store.obj1_col
#print(y.head())
store.put('obj2',frame,format='table')
store.select('obj2',where=['index>10'])  # if table format i can condition here
print(store.obj2.head())
'''
import requests
import json
'''
url="http://search.twitter.com/search.json?q=python%20pandas"
resp=requests.get(url)
print(resp)
data=resp.json()
print(data)
res=json.load(resp)
'''
import sqlite3   # rdbms
#creating table
query="""CREATE TABLE test (a VARCHAR(20),b VARCHAR(20),c REAL,d INTEGER);"""
con=sqlite3.connect('mydata1.sqlite3')
#con.execute(query)
con.commit()
data=[('atlanata','georgia',1.25,6)]
smtp="INSERT INTO test Values(?,?,?,?)"
con.executemany(smtp,data)
cursor=con.execute("SELECT * FROM test")
print(cursor.description)
file=pd.read_csv("C:/Users/Haroon Traders/Desktop/Assignment-2/Euro_2012_stats_TEAM.csv")
file