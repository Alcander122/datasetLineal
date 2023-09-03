#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[27]:


reg= pd.read_csv("C:/Users/cali_/Downloads/archive (1)/framingham.csv")
reg.dropna(axis=0, inplace=True)
X=reg.iloc[:,:-1].values
y=reg.iloc[:,-1].values
reg.head()


# In[29]:


reg.isnull().sum()


# In[31]:


reg_1=reg[reg['TenYearCHD']==1]
reg_2=reg[reg['TenYearCHD']==0]
print(reg_1['glucose'].mean()-reg_2['glucose'].mean())


# In[33]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.30,random_state=42)


# In[35]:


import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = reg.cigsPerDay 

# Create a distribution plot
sns.histplot(data, kde=True, color='blue')

# Add labels and title
plt.xlabel('cigsPerDay  Value')
plt.ylabel('Frequency')
plt.title('Distribution Plot')

# Display the plot
plt.show()


# In[37]:


median_value_cigsPerDay = reg['cigsPerDay'].median()

print("Median:", median_value_cigsPerDay)


# In[39]:


reg['cigsPerDay'].fillna(median_value_cigsPerDay , inplace=True)


# In[41]:


data = reg.BPMeds

# Create a distribution plot
sns.histplot(data, kde=True, color='blue')

# Add labels and title
plt.xlabel('BPMeds  Value')
plt.ylabel('Frequency')
plt.title('Distribution Plot')

# Display the plot
plt.show()


# In[43]:


reg["BPMeds"].fillna(0,inplace=True)


# In[44]:


reg.isnull().sum()


# In[46]:


data = reg.glucose

# Create a distribution plot
sns.histplot(data, kde=True, color='blue')

# Add labels and title
plt.xlabel('glucose  Value')
plt.ylabel('Frequency')
plt.title('Distribution Plot')

# Display the plot
plt.show()


# In[51]:


df_cleaned = reg.dropna(subset=['glucose','BMI'])
df_cleaned.shape


# In[52]:


correlation_matrix = df_cleaned.corr()
correlation_matrix


# In[53]:


plt.figure(figsize=(14, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()

