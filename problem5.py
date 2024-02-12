#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


Housing = pd.read_csv(r"C:\Users\Lenovo\Desktop\seaborn-data\housing1.csv.xls")
Housing


# In[11]:


Housing['median_house_value'].info()


# In[30]:


sns.histplot(Housing['median_house_value'], kde=True, bins=30,color = 'r')


# * This distribution has positive skewness it means that the data is leaning towards higher values
# * The graph shows that there are more occurrences of higher house prices compared to the ones that are lower

# In[31]:


tips = pd.read_csv(r"C:\Users\Lenovo\Desktop\seaborn-data\tips.csv")
tips


# In[33]:


sns.histplot(tips['total_bill'], kde=True, bins=30,color = 'r')


# In[ ]:




