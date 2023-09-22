#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 08:47:29 2023

@author: sq
"""

import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

# method 1 to read Json data

json_file = open('loan_data_json.json')
data = json.load(json_file)


# method 2 to read Json data

with open('loan_data_json.json') as json_file:
    data= json.load(json_file)
    
#trnsforme to dataframe
loandata = pd.DataFrame(data)

#finding unique values purpose col
loandata['purpose'].unique()

#desc the data
loandata.describe()

#desc the data for specific col
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#create a col using exp to get annula income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#working with arrays
#1d array
arr = np.array([1,2,3,4])

#0d arrary
arr = np.array(43)

#2d array
arr = np.array([[1,2,3],[4,5,6]])



#working with if statements
a= 40 
b = 500
 
if b > a:
   print('b is greater than a')     

#more conditions
a=24
b=500
c=1000

if b > a and b < c:
    print('b is greater than a but less than c')
    

#what if condition is not met
a = 40
b = 500
c = 20
    
    
if b > a and b < c:
     print('b is greater than a but less than c')
else:
    print('no conditions met')
    
    
#another condition different matrix
a=40
b=0
c=30

if b>a and b<c:
    print('b is greater than a but less than c')
elif b>a and b>c:
    print('b is greater than a and c')
else:
    print('no conditions met')
    

#using or
a=40
b=500
c=30

if b>a or b<c:
    print('b is greater than a but less than c')

else:
    print('no conditions met')
    

#fico score

fico = 250

if fico >= 300 and fico < 400:
    ficocat = 'very poor'
elif fico >= 400 and fico < 600:
    ficocat ='Poor'
elif fico >= 600 and fico < 660:
    ficocat ='fair'
elif fico >= 660 and fico < 700:
    ficocat ='good'
elif fico >= 700:
    ficocat ='Excillent'
else:
    ficocat = 'unknown'
    
print(ficocat)
    
#for loop

fruits = ('apple','pear', 'banana', 'cherry')

for x in fruits:
    print(x)
    y = x+' fruit'
    print(y)
    
for x in range(0,4):
    y = fruits[x] + ' for sate'
    print(y)


#applying for loops to loan data
#using first 10
# Try - used to make python try to run a statement
ficocat = []
length = len(loandata)
for x in range(0,length):
    catagory = loandata['fico'][x]
    try:
        if catagory >= 300 and catagory < 400:
           cat = 'very poor'
        elif catagory >= 400 and catagory < 600:
           cat = 'poor'
        elif catagory >= 601 and catagory < 660:
           cat = 'fair'
        elif catagory >= 601 and catagory < 700:
            cat = 'good'
        elif catagory >= 700 :
           cat = 'excillent' 
        else:
           cat = 'unknown'        
    except:
        cat = 'unknown'
    ficocat.append(cat)

# print(ficocat)

ficocat = pd.Series(ficocat) 

loandata['fico.catagory'] = ficocat




#df.loc as conditional statements
#df.loc[d[columnname] condition, newcolumnname']= 'value if condition is met
    
    
 #for interest rate a new column is needed if the rate is > 0.12 high else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type' ]   = 'high'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type' ]   = 'low'


#number of loans by fico catagory

catplot = loandata.groupby(['fico.catagory']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

purposeplot = loandata.groupby(['purpose']).size()
purposeplot.plot.bar(color = 'red', width = 0.2)
plt.show()


#scattre plots

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color ='red') # you can use hex color name format as well
plt.show

#writing to CSV
loandata.to_csv('loan_cleaned.csv',index = True)
























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




































