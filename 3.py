import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
path='data_to_clean.csv'
df=pd.read_csv(path)

none= mydata.isnull().sum().sort_values(ascending=False)
print(none)#缺失值

notKnow=["?"]
notNumber = mydata.isin(notKnow).sum().sort_values(ascending=False)
print(notNumber)#缺失值

#散点
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(8,7))
plt.scatter(mydata['ID'],mydata['RevolvingUtilizationOfUnsecuredLines'],marker='o')
plt.show()

x6=list(df['NumberOfTimes90DaysLate'])
x7=list(df['NumberOfTimes90DaysLate.1'])

for i in x6:
    try:
        i=int(i)
    except:
        i=200
for i in x7:
    try:
        i=int(i)
    except:
        i=200
print(type(x6))

plt.figure(figsize=(8,5))
plt.scatter(x6,x7,marker="o")
plt.show()
