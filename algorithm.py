#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=pd.read_excel('data.xlsx')


# In[4]:


info=dict() 


# In[5]:


info1 = dict([('name', 1), ('color', 2), ('time', 3), ('good', '校园卡'), ('place', '食堂')])


# In[8]:


def matching(info):
    res=pd.DataFrame()
    j=0
    for i in range(0,len(data)):
        if (info1['good']==data['good'][i]):
            res[j]=data.loc[i]
            j=j+1
    res1=pd.DataFrame(np.array(res).transpose(1, 0))
    res1.columns=['name','color', 'time', 'good','place']
    return res1


# In[9]:


matching(info1)

