#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as graf
import numpy as np
import os


# In[3]:


inf= pd.read_csv("C:/Users/cali_/Downloads/archive/car_data.csv")


# In[4]:


inf


# In[5]:


print (inf.count())


# In[6]:


inf.dtypes


# In[28]:


graficaCar= graf.figure(figsize=(20,20))
graf.title("Datos_De_Carro")

(inf.groupby(["Car_Name"]) ["Kms_Driven"].sum()).plot(kind="barh", alpha=0.5)


# In[ ]:




