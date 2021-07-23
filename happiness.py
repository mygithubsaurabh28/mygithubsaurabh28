#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data=pd.read_csv(r"E:\data trained projects\happiness_score_dataset.csv")


# In[3]:


data.head()


# In[4]:


data.shape


# In[5]:


data.isnull().sum()


# In[6]:


data.describe()


# In[7]:


data=data.drop(columns=['Region'])


# In[8]:


data


# In[9]:


x=['Happiness Rank','Happiness Score','Standard Error','Economy (GDP per Capita)','Family','Health (Life Expectancy)','Freedom','Trust (Government Corruption)','Generosity','Dystopia Residual']
x


# In[10]:


plt.figure(figsize=(25,25))
graph=1
for column in x:
    if graph<=10:
        ax=plt.subplot(6,4,graph)
        sns.boxplot(data[column],orient='v')
        plt.xlabel(column,fontsize=15)
    graph+=1
plt.show()


# In[11]:


q1=data['Standard Error'].quantile(0.25)
q3=data['Standard Error'].quantile(0.85)
q1,q3


# In[12]:


iqr=q3-q1


# In[13]:


q1=data['Family'].quantile(0.25)
q3=data['Family'].quantile(0.85)
q1,q3


# In[14]:


q1=data['Trust (Government Corruption)'].quantile(0.25)
q3=data['Trust (Government Corruption)'].quantile(0.85)
q1,q3


# In[15]:


q1=data['Generosity'].quantile(0.25)
q3=data['Generosity'].quantile(0.85)
q1,q3


# In[16]:


q1=data['Dystopia Residual'].quantile(0.25)
q3=data['Dystopia Residual'].quantile(0.85)
q1,q3


# In[17]:


lower_limit= q1-1.5*iqr
upper_limit= q3+1.5*iqr


# In[18]:


no_outlier_standard=data[(data['Standard Error']<lower_limit)|(data['Standard Error']>upper_limit)]


# In[19]:


data['Standard Error']=no_outlier_standard


# In[20]:


no_outlier_Family=data[(data['Family']<lower_limit)|(data['Family']>upper_limit)]


# In[21]:


data['Family']=no_outlier_Family


# In[22]:


no_outlier_Trust=data[(data['Trust (Government Corruption)']<lower_limit)|(data['Trust (Government Corruption)']>upper_limit)]


# In[23]:


data['Trust (Government Corruption)']=no_outlier_Trust


# In[24]:


no_outlier_Generosity=data[(data['Generosity']<lower_limit)|(data['Generosity']>upper_limit)]


# In[25]:


data['Generosity']=no_outlier_Generosity


# In[26]:


no_outlier_Dystopia=data[(data['Dystopia Residual']<lower_limit)|(data['Dystopia Residual']>upper_limit)]


# In[27]:


data['Dystopia Residual']=no_outlier_Dystopia


# In[34]:


data


# In[ ]:





# In[ ]:




