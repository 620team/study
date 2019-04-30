#!/usr/bin/env python
# coding: utf-8

# In[60]:


from faker import Faker
import pandas as pd
import random


# In[3]:


f=Faker(locale='zh_CN')
mydata=pd.read_excel('data.xlsx')


# In[38]:


name=[]
for i in range(0,100):
    name.append(f.name())


# In[41]:


color=[]
for i in range(0,100):
    color.append(f.color_name())


# In[43]:


time=[]
for i in range(0,100):
    time.append(f.past_date())


# In[69]:


mydata['name']=name
mydata['color']=color
mydata['time']=time
mydata['good']=good
mydata['place']=place


# In[62]:


goods=['手机','耳机','校园卡','钱包','书','配饰','钥匙','衣服','U盘','电脑','帽子','笔袋','眼镜','其他']
good=[]
for i in range(0,100):
    good.append(random.sample(goods,1))


# In[66]:


places=['食堂','图书馆','教室','宿舍楼','篮球场','饮水处','洗手间','排球场','网球场','操场','超市','打印店','机房']
place=[]
for i in range(0,100):
    place.append(random.sample(places,1))


# In[72]:


mydata.to_excel('data.xlsx')

