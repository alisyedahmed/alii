#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[8]:


df = pd.read_csv('world_demographics.csv.zip')


# In[9]:


df.head()


# In[12]:


# Assuming you have a column named 'Age' in your dataset
# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['Age'], df['Source Year'], color='skyblue')
plt.xlabel('Age')
plt.ylabel('Source Year')
plt.title('Age Distribution')
plt.xticks(df['Age'])
plt.grid(True)
plt.show()


# In[11]:


# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.grid(True)
plt.show()


# In[ ]:




