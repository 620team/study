#!/usr/bin/env python
# coding: utf-8

# In[1]:


from faker import Faker
import pandas as pd
import random


# In[2]:


f=Faker(locale='zh_CN')


# In[3]:


name=[]
for i in range(0,100):
    name.append(f.name())


# In[4]:


color=[]
for i in range(0,100):
    color.append(f.color_name())


# In[5]:


time=[]
for i in range(0,100):
    time.append(f.past_date())


# In[6]:


goods=('手机','耳机','校园卡','钱包','书','配饰','钥匙','衣服','U盘','电脑','帽子','笔袋','眼镜','其他')
good=[]
for i in range(0,100):
    good.append(random.sample(goods,1))


# In[7]:


newgood=[]
for i in range(0,len(good)):
    newgood.append(' '.join(good[i]))


# In[8]:


places=['食堂','图书馆','教室','宿舍楼','篮球场','饮水处','洗手间','排球场','网球场','操场','超市','打印店','机房']
place=[]
for i in range(0,100):
    place.append(random.sample(places,1))


# In[9]:


newplace=[]
for i in range(0,len(place)):
    newplace.append(' '.join(place[i]))


# In[12]:


mydata=pd.DataFrame()
mydata['name']=name
mydata['color']=color
mydata['time']=time
mydata['good']=newgood
mydata['place']=newplace


# In[14]:


mydata.to_excel('data.xlsx')

