#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd


# In[74]:


df = pd.read_excel("C:/Users/Envy 360/Downloads/AGN02.xls")


# In[75]:


df.head


# In[77]:


writer = pd.ExcelWriter('dataframe.xls', engine='xlsxwriter')
df.to_excel(writer, sheet_name='mynewdata')
writer.save()


# In[71]:


df.head


# In[ ]:





# In[ ]:




