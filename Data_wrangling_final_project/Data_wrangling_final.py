#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
url=r"C:\Users\Aakash\Desktop\Data wrangling\owid-covid-data.csv"
df= pd.read_csv(url)


# In[2]:


num_rows,num_cols = df.shape
print("Number of rows:",num_rows)
print("Number of columns:",num_cols)


# In[3]:


print("\nData types of columns:")
print(df.dtypes)


# In[4]:


print("\nInfo:")
print(df.info())

print("\nDescribe:")
print(df.describe())


# In[5]:


Unique_values = df['location'].nunique()
print("\nCount of unique values in the  location coloumn:",Unique_values)


# In[6]:


con_frequency = df['continent'].value_counts()
con_with_max_frequency = con_frequency.idxmax()
print("\ncontinent with maximum frequency:",con_with_max_frequency)


# In[7]:


max_cases = df['total_cases'].max()
mean_cases = df['total_cases'].mean()
print("\nMaximum value in 'stotal_cases':",max_cases)
print("\nMean value in 'total_cases':",mean_cases)


# In[8]:


quartiles_total_deaths = df['total_deaths'].quantile([0.25,0.5,0.75])
print("\n25% Quartile values in 'total_deaths':",quartiles_total_deaths[0.25])
print("\n50% Quartile values in 'total_deaths':",quartiles_total_deaths[0.5])
print("\n60% Quartile values in 'total_deaths':",quartiles_total_deaths[0.75])


# In[9]:


contient_with_max_hdi = df.loc[df['human_development_index'].idxmax(),'continent']
print("\ncontinent with maximum 'human_development_index':",contient_with_max_hdi)


# In[10]:


contient_with_min_gdp = df.loc[df['gdp_per_capita'].idxmin(),'continent']
print("\ncontinent with minimum 'gdp_per_capita':",contient_with_min_gdp)


# In[11]:


selected_columns = ['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']
df = df[selected_columns]
print(df)


# In[12]:


df = df.drop_duplicates()
print(df)


# In[13]:


missing_values = df.isnull().sum()
print("\nMissing values:")
print(missing_values)


# In[15]:


df = df.dropna(subset=['continent'])
print(df)


# In[16]:


df = df.fillna(0)
print(df)


# In[18]:


df['date'] = pd.to_datetime(df['date'])


# In[19]:


df_groupby = df.groupby('continent').max().reset_index()


# In[20]:


df_groupby['total_deaths_to_total_cases'] = df_groupby['total_deaths'] / df_groupby['total_cases']


# In[21]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[22]:


plt.figure(figsize=(8,6))
sns.distplot(df_groupby['gdp_per_capita'],bins=10,kde=False)
plt.xlabel('GDP_per_capita')
plt.ylabel('Frequency')
plt.title('Histogram of GDP_per_capita')
plt.show()


# In[23]:


plt.figure(figsize=(8,6))
plt.scatter(df['gdp_per_capita'],df['total_cases'])
plt.xlabel('GDP per capita')
plt.ylabel('Total cases')
plt.title('Scatter plot of total cases vs. GDP per capita')
plt.show()


# In[24]:


sns.pairplot(df_groupby)
plt.show()


# In[25]:


plt.figure(figsize=(10,6))
sns.catplot(x='continent', y='total_cases',kind='bar', data=df_groupby)
plt.xlabel('Continent')
plt.ylabel('Total cases')
plt.title('bar plot of Total Cases by Continent')
plt.show()


# In[ ]:




