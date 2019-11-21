# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 14:27:55 2019

@author: Haroon Traders
"""
import pandas as pd

from numpy import nan as NA
import numpy as np

data = pd.DataFrame([[1., 6.5, NA], [1., NA, NA], 
                     [NA, NA, NA], [NA, 6.5, NA]], 
                    columns = list('abc'))
#display(data)
#remoe all rows that have null values
cleaned = data.dropna()

#how = all = remove rows only all data is NaN
#cleaned = data.dropna(how='all')   #to delete the nan values if all are nan in the same row
#print(cleaned)
print() # blank line
#print(cleaned)

#Passing how='all' will only drop rows that are all NA:
#data.dropna(how='all')

# dropping columns that have all null values
#cleaned_Col=data.dropna(axis=1) #remove the complete row if any of the NAN
cleaned_col=data.dropna(axis=1, how='all')
print(cleaned_col)  #cleaned the axix1 -->columns if all having nan
df = pd.DataFrame(np.random.randn(7, 3))
#print(df)
#df.iloc[:4, 1] = NA   #accessing through position
df.iloc[:2, 2] = NA   #accessing through position
#display(df)
ab=df.fillna(1.5)  #filling 1.5 in place of nan
#display(ab)
# column number 1 will be filled with 0.5
# column number 2 will be fileld with 0
#df = df.fillna({1: 0.5, 2: 0})
#display(df)
# fill  not values from left column (axis=0 means from top row)
#df = df.fillna(method='ffill',axis=1)  #forward fill  #here backward fill works palce all non none values to nan in forward or backwared order
#display(df)
df = df.fillna(method='ffill', limit=1, axis=1)  #only one value canbe none
#display(df)
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]} )
#display(data)
#print(data.duplicated())  #check row wise
data = data.drop_duplicates()
#display(data)
df1 = pd.DataFrame(np.random.randn(7, 3))

df1.iloc[:4, 1] = np.nan
df1.iloc[:2, 2] = np.nan
#display(df1)
df1 = df1.replace(np.nan , -999)
#display(df1)
df1 = df1.replace(-999 , -9)
#display(df1)
df2 =df1.replace([-999, -9],[101, 0])  #-999-->101  -9-->0  
#display(df2)
data = pd.DataFrame(np.random.randn(500, 4))
data.describe()
col = data[2]
#print(col)
col[np.abs(col) > 3]
#To select all rows having a value exceeding 3 or –3, 
#you can use the 'any' method on a boolean DataFrame:
#any method will check all cells 
outliers = data[(np.abs(data) > 3).any(1)]
print(len(outliers), len(data))
print(outliers)
# check the difference
#print(data)
#data[(np.abs(data) > 3)]
data = pd.DataFrame(np.arange(12).reshape((3, 4)),
        index=['Ohio', 'Colorado', 'New York'],
        columns=['one', 'two', 'three', 'four'])
def transforms_alt(label):
    new_label=label[:4].upper()
    return new_label
#display(data)
#transform = lambda x: x[:4].upper()  #four alphabets pick
data.index= data.index.map(transforms_alt) #work on index label of index comes in transform
display(data)
import re
text = "foo    bar\t baz \tqux"
normal_split = text.split()
print(normal_split)
ab=re.split('\s+', text) # spliting based on whitespaces
print(ab)
print(text.split(" "))
#['foo', 'bar', 'baz', 'qux']
# compile once to use again and again and save time
rgx = re.compile('\s+')
print(rgx.split(text))
data = ["simpleEmail@email.com",   "simple.email@email.com",  
        "plus+symbol@email.com",   "dash-symbol@email.com",  
     "q@email.com",   
    "“unusual”@email.com",   "dash-symbol@email-dash.com",   "test@emailServer",  
  "” “@email.com",   "user@[IPv6:2001:DB8::1]",   
  "example@localhost",   "example@s.solutions",   
  "12345@email.com"]   

data = pd.Series(data)
display(data)
pattern = '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,4})'  #email checking authentic or not
abd=data.str.findall(pattern, flags=re.IGNORECASE)
print(abd) #checking email
matches = data[data.str.match(pattern, flags=re.IGNORECASE)]
print(matches)
df2=pd.DataFrame(a)
print(df2)