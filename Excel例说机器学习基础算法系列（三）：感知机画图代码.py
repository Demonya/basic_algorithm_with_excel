#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


# In[2]:


data = pd.DataFrame([[3,3,1],[4,3,1],[1,1,0]])
color1 = ['g','g','orange']
data.iloc[:,2:3]


# In[3]:


x = np.arange(1,5) 
color = ['black','gray','navy','orange','slategrey','midnightblue','green']
y =  [(-1-3*x)/3,-x,1-x,0*x-2,(1-3*x)/3,(2-2*x)/2,3-x]
plt.figure(figsize=(10,7))
for i in range(len(y)):
    plt.scatter(data.iloc[:,0:1],data.iloc[:,1:2],c=color1)
    plt.plot(x,y[i], color=color[i],label = 'epoch ' + str(i+1))
plt.legend()
plt.grid()
plt.show()


# In[4]:


x = np.arange(1,5) 
color = ['black','gray','navy','orange','slategrey','midnightblue','green']
y =  [(-1-3*x)/3,-x,1-x,0*x-2,(1-3*x)/3,(2-2*x)/2,3-x]
plt.figure(figsize=(10,7))
for i in range(len(y)):
    plt.scatter(data.iloc[:,0:1],data.iloc[:,1:2],c=color1)
    plt.plot(x,y[i], color=color[i],label = '第 ' + str(i+1) + '次迭代')
    plt.legend()
    plt.grid()
    plt.show()


# In[ ]:




