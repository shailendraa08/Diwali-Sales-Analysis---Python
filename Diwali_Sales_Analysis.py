#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[13]:


df = pd.read_csv('Diwali_Sales_Data.csv', encoding='latin-1')
df.shape


# In[14]:


df.head()


# In[15]:


df.info()


# In[17]:


pd.isnull(df).sum()


# In[21]:


df.shape


# In[19]:


df.dropna(inplace=True)


# In[22]:


# Change Data Type
df['Amount'] = df['Amount'].astype('int')


# In[24]:


df['Amount'].dtypes


# In[25]:


df.columns


# In[26]:


# Rename Columns
df.rename(columns= {'Marital_Status':'Shaadi'})


# In[37]:


df.rename(columns= {'Shaadi':'Marital_Status'})


# In[27]:


# describe() method returns description of the data in the Dataframe(i.e count,mean,std, etc)
df.describe()


# In[28]:


# use describe() for specific columns
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# # Gender

# In[29]:


ax = sns.countplot(x = 'Gender', data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x= 'Gender', y= 'Amount', data = sales_gen)


# From the above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than males.

# # Age

# In[31]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[32]:


#Total AMount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x= 'Age Group', y= 'Amount', data = sales_age)


# From above graph we can see that most of the buyers are of age group between 26-35 years female

# # State

# In[33]:


#total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data= sales_state, x= 'State', y = 'Orders')


# In[35]:


# total amount/sales from top10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State', y='Amount')


# From above graphs we can see that most of the orders are from Uttar Pradesh, Maharashtra and Karnataka respectively.

# # Marital Status

# In[41]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[40]:


sales_state = df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(7,5)})
sns.barplot(data = sales_state, x = 'Marital_Status', y='Amount', hue='Gender')


# From the above graphs we can see that most of the buyers are married(women) and they have high purchasing power

# # Occupation

# In[43]:


ax = sns.countplot(data = df, x = 'Occupation')

sns.set(rc={'figure.figsize':(20,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[44]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation', y='Amount')


# From the above graphs we can see that most of the buyers are working in IT, Aviation and Healthcare sector

# # Product Category

# In[47]:


ax = sns.countplot(data = df, x = 'Product_Category')

sns.set(rc={'figure.figsize':(20,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[48]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category', y='Amount')


# From the above graphs we can see that most of the sold products are from Food, Footwear and Electronics Category

# In[50]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID', y='Orders')


# In[51]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion:

# Married women age group 26-35 years from UP,Maharashtra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from food, clothing and electronics category.

# In[ ]:




