#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df=pd.read_csv("retail_sales_dataset.csv")


# In[4]:


df.head(5)


# In[5]:


df.describe(include='all')


# In[6]:


df.dtypes


# In[7]:


df.isna().sum()


# In[8]:


df.count()


# In[9]:


df.shape


# In[10]:


df["Gender"].value_counts()


# In[11]:


df["Product Category"].value_counts()


# In[12]:


df["Age"].value_counts()


# In[14]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df['Date']=pd.to_datetime(df['Date'])

# Calculate total sales over time
monthly_sales = df.groupby(df['Date'].dt.to_period("M")).agg({'Total Amount':'sum'})

# Plotting
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='bar')
plt.title('Total Sales Over Time (Monthly)')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


# In[15]:


sales_by_category = df.groupby('Product Category').agg({'Total Amount':'sum'})

# Plotting
plt.figure(figsize=(8, 6))
sales_by_category.plot(kind='bar')
plt.title('Sales Distribution Across Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


# In[16]:


sales_by_gender = df.groupby('Gender')['Total Amount'].sum()

# Make sure 'sales_by_gender' is a pandas Series
print(type(sales_by_gender))  # This should output: <class 'pandas.core.series.Series'>

# Now plot the pie chart directly from the Series
sales_by_gender.plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales by Gender')
plt.ylabel('')  # This hides the y-axis label, which is not needed for pie charts
plt.show()


# In[17]:


bins = [0, 18, 30, 40, 50, 60, 100]
labels = ['0-18', '19-30', '31-40', '41-50', '51-60', '60+']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

sales_by_age_group = df.groupby('Age Group').agg({'Total Amount':'sum'})

# Plotting
plt.figure(figsize=(10, 6))
sales_by_age_group.plot(kind='bar')
plt.title('Sales by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


# In[19]:


total_revenue_by_category=df.groupby('Product Category')['Total Amount'].sum()
total_revenue_by_category


# In[20]:


average_revenue_by_category=df.groupby('Product Category')['Total Amount'].mean()
average_revenue_by_category


# In[21]:


quantity_sold_by_category=df.groupby('Product Category')['Quantity'].sum()
quantity_sold_by_category


# In[ ]:




