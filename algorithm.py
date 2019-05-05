#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=pd.read_excel('data1.xlsx')


# In[3]:


info=dict() 


# In[4]:


info1 = dict([('name', 1), ('color', 2), ('time', 3), ('good', '校园卡'), ('place', '食堂')])


# In[5]:


def matching(info):
    res=pd.DataFrame()
    ress=pd.DataFrame()
    j=0
    q=0
    for i in range(0,len(data)):
        if (info1['good']==data['good'][i]):
            res[j]=data.loc[i]
            j=j+1
    res1=pd.DataFrame(np.array(res).transpose(1, 0))
    res1.columns=['name','color', 'time', 'good','place']
    if j>5:
        for k in range(0,len(res1)):
            if (info1['place']==res1['place'][k]):
                ress[q]=res1.loc[k]
                q=q+1
        res2=pd.DataFrame(np.array(ress).transpose(1, 0))
        res2.columns=['name','color', 'time', 'good','place']
        return res2  
    else:
        return res1


# In[6]:


matching(info1)

