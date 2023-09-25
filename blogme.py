#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 08:37:51 2023

@author: sq
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel files
data = pd.read_excel('articles.xlsx')

#summary of the data
data.describe()

#summary of the columns
data.info()

#group by function - counting number of articles
#format - df.groupby{['column to groupby']},['column to count/sum'].count()

data.groupby(['source_id'])['article_id'].count()

#number of reacton by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#drop column
data = data.drop('engagement_comment_plugin_count', axis = 1)


#functions in python

def thisfunction():
    print('this is my first function')

thisfunction()

#this is a function with variables

def aboutme(name, lastname, location):
    print('this is '+name+' my last name is '+lastname+ ' i am from '+location)
    return name, lastname, location

a = aboutme('sally','qureshi','US')

#use for loops in function

def favfood(food):
    for x in food:
        print('top food is '+x)

fastfood =['burgers','pizza','pie']    

favfood(fastfood)


#creating a keyword flag

keyword = 'crash'

# creat function to isolat each title row

# length = len(data)
# keyword_flag = []
# for x in range(0,length):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)  #append the keyword



def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag) 
    return keyword_flag

keywordflag = keywordflag('murder')

#creating new col in data dataframe

data['keyword']= pd.Series(keywordflag)

#SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']


#add for loop to extract sentiment

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)

for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        nue = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment


#write data

data.to_excel('blogme_clean.xlsx', sheet_name = 'blogmedata', index=False)

































