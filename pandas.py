# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:11:11 2019

@author: Haroon Traders
"""

import pandas as pd
'''
abc=['faraz',123,[3,4,5]]
print(abc)
print(type(abc))    #0ne dim array is series
a=pd.Series(abc)
print(a.values)
print(a.index)
print(a) #converting other data types into 1d array
print(type(a))
dict={'key1':["faraz","umer","uroosa"],'key2':["maryam","hammad","ayesha"]}
print(type(dict))
print(pd.Series(dict))
print(type(pd.Series(dict)))
df=pd.DataFrame(dict)
print(df)
se=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(se)
#create pandas series to store canteen data
import calendar as cal
b=list(cal.day_name)
canteen=pd.Series([23,34,55,66,77,88,99],index=b)
canteen["abc"]=123   #add column
print(canteen)
print(canteen[['Thursday','Friday']])
print(canteen.unique)
dict1={'sindh':123}
ch=pd.Series(dict1,index=b)
print(ch)   #only in dictionery you can add more index than values
print(pd.isnull(ch))
data = { 'name' : ['AA', 'IBM', 'GOOG'], 'date' : ['2001-12-01', '2012-02-10', '2010-04-09'], 'shares' : [100, 30, 90], 'price' : [12.3, 10.3, 32.2] }
a=pd.DataFrame(data)
a.index=['one','two','three']
a.set_index(["name"])
print(a)
abd=pd.Series({'laiba':4,'umer':2})
abd1=pd.Series({'laiba':5,'umer':2})
print(abd+abd1)   #adding similar data
'''
import calendar as cal
b=list(cal.day_name)
apples=pd.Series([3,5,6,4])
oranges=pd.Series([1,8,6,3])
data={"apples":apples,"oranges":oranges}
fruit_df=pd.DataFrame(data)  #index should be matched ,index=b
#print(fruit_df)


state=["ohio","ohio","ohio","pak","pak","pak"]
data={"state":state,"year":[2000,2001,2002,2003,2004,2005],"pop":[1.5,1.7,3.6,2.4,2.9,3.2]}
result=pd.DataFrame(data,index=['1st','2nd','3rd','4th','5th','6th'],columns=["pop","year","state","random"])
#print(result)
#print(result["pop"]) #return the desired coloums
#print(result.head()) #return the default start 5 values untill desired value is entered
#print(result.tail()) #return the default last 5 values untill desired value is entered
#result["random"]["1st"]=3.3
#print(result)
#print(result.ix["3rd"])
ln=len(result)
#print(ln)
import numpy as np
arr=np.arange(ln)
#print(arr)
result["random"]=arr
#print(result)
val = pd.Series([-1.2, -1.5, -1.7], index=['2nd', '4th', '5th'])
result["random"]=val
#print(result)
obj3=pd.Series(['blue','purple','yellow'],index=[0,3,6])
#print(obj3)
#obj3=obj3.reindex(range(9))#method='bfill')
#print(obj3)
obj3=obj3.reindex(range(9),method='bfill')  #ffill=forward fill and bfill = backward fill
#print(obj3)
result['eastern'] = result.state == 'ohio'
#print(result)
del result['eastern']  # delete the desired column same as dicti and list
#print(result)
rand=pd.DataFrame(np.arange(9).reshape(3,3),index=['a','c','d'],columns=['ohio','texas','california'])
#print(rand)
#print(np.arange(9).reshape(3,3))
result=result.drop('pop',axis=1,inplace=True)
#print(result)
dataframe=pd.DataFrame(np.arange(16).reshape(4,4),index=['pakistan','india','japan','usa'],columns=['one','two','three','four'])
#print(dataframe)
df2=dataframe[['one','two']]
#print(df2)
#print(dataframe[2:])  #row wise
a=dataframe.one[2:]
#print(a)
ab=dataframe.loc[['pakistan'],['one','two']] #fancy indexing  accessing values through columns
#print(ab)
#print(dataframe.iloc[2,2])  #accessing values  through indexes
# function applcation and mapping
def min_max(col):   #column wise operation
    minimun=col.min()
    maximum=col.max()
    #return minimun,maximum
    return pd.Series([np.abs(minimun-maximum)],index=['value'])
#abb=dataframe.apply(min_max)
#print(abb)
# alternate work fro above function
f=lambda x:x.min()-x.max()
abb=dataframe.apply(f)
#print(abb)
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj)
print(obj.sort_index())
print(obj.sort_values(axis=0))  #axis=0 row wise
dict={'key1':["faraz","umer","uroosa"],'key2':["maryam","hammad","ayesha"]}
df=pd.DataFrame(dict)
print(df)
import pandas as pd
abc=[75,80,79,60]
marks=pd.Series(abc)
marks
from numpy import nan as na
dic={'students':['faraz','umer','uroosa','hashir','abdur rehman','laiba','moiz'],'id':[1,2,3,4,5,6,7],'marks':[55,56,88,45,33,na,100]}
ind=['a','b','c','d','e','f','g']

df=pd.DataFrame(dic,index=ind)
df
file=pd.read_csv("C:/Users/Haroon Traders/Desktop/Assignment-2/Euro_2012_stats_TEAM.csv")
file
df.columns
from numpy import nan 
a=dic['marks']
for b in range(0,len(a)-1):
    #temp_max=a[0]
    if a[b]>a[b+1]:
        temp_max=a[b+1]
        a[b+1]=a[b]
        a[b]=temp_max
#print(a)
a.sort()      
f=len(a)
print(f)
for x in range(0,f):
    if a[x]==nan:
        a[x]=0
print(a)
df2=pd.DataFrame(a)
print(df2)