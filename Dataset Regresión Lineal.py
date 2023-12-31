#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

length = 4 

df = pd.read_csv('C:/Users/cali_/Downloads/archive/data.csv', index_col=False, header=0)
x = df.metro.values
y = df.precio.values

print(df)

x = x.reshape(length, 1)
y = y.reshape(length, 1)


# In[10]:


# Regresion
regr = linear_model.LinearRegression()
regr.fit(x, y)

 
print( "a: %s"%(regr.intercept_[0]))
print( "b: %s"%(regr.coef_[0][0]))

X_predict = [[35]]
y_predict = regr.predict(X_predict)

print("Prediccion. Si x=%s entonces y=%s" % (X_predict[0][0], y_predict[0]))


# In[8]:


plt.scatter(x, y,  color='black')
plt.plot(x, regr.predict(x), color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()


# In[ ]:




