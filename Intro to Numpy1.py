#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[6]:


a=np.arange(24).reshape(4,6)
a


# In[11]:


np.vsplit(a,2)


# In[12]:


import pandas as pd


# In[13]:


numbers = range(1,100,5)
numbers


# In[16]:


a = pd.Series(numbers)
a


# In[22]:


string = ("HI","HOW","ARE","YOU","?")
string


# In[24]:


pd.Series(string)


# In[27]:


S = pd.Series([365, "HAPPY BDAY", -23.5,23.5])
S


# In[30]:


MARKS = [80,90,75,78,96]
SUBJECT = ["MATHS", "SCIENCE", "KISWAHILI","SOCIAL SCIENCE", "ENGLISH"]
pd.Series(MARKS,SUBJECT)


# In[31]:


pd.Series(SUBJECT,MARKS)


# In[34]:


pd.Series(index = MARKS,SUBJECT)


# In[ ]:


SUBJECT1 = 

