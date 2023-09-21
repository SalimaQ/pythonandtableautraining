#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:32:25 2023

@author: sq
"""

import pandas as pd

#file_name = pd.read.csv('file.csv') <format to read a csv file>

#data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv',sep=';')

#summary of the data

data.info()

#working with calclations
#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical operation on tableau

ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction  = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

#cost per trasaction column calc

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = NumberOfItemsPurchased * CostPerItem

#add column to dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']
data['SelesPricePerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']
data['ProfitPerTransaction'] = data['SelesPricePerTransaction'] - data['CostPerTransaction']
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction'] 

#Rounding Markup
data['Markup'] = round(data['Markup'],2)

#combine data fields

#my_date = data['Day']+ '-'   

#check column type
print(data['Day'].dtype)

#Change column Type
day = data['Day'].astype(str)
year =data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'+ data['Month']+'-'+ year
data['date']= my_date

#using ilock to view specific columns

data.iloc[0] #use the rows with index 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #first 5 rows

data.iloc[:,2] #all rows for 2 column

data.iloc[4,2] #4th row 2nd column

#split function for client keywork columns
#new_var = column.str.split('sep',expand = true)

split_col = data['ClientKeywords'].str.split(',',expand=True)

#creating new cols for split col in client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['ContractLength'] = split_col[2]


# Replace function

data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['ContractLength'] = data['ContractLength'].str.replace(']','')

#using the lower functions to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()



# How to merge files

#bringing in new dataset Value_inc_seasons.csv

seasons = pd.read_csv('Value_inc_seasons.csv',sep=';')


#merging files: merge_df = pd.merge(df_old, df_new, on = 'Key')

data = pd.merge(data, seasons, on = 'Month')



#drop columns from dataframe
# df = df.drop('columnname',axis =1)

data = data.drop('ClientKeywords', axis =1)
data = data.drop('Day', axis =1)

#drop multiple columns
data = data.drop(['Month','Year'], axis =1)


#export into csv

data.to_csv('ValueInc_cleaned.csv', index = False)

















































