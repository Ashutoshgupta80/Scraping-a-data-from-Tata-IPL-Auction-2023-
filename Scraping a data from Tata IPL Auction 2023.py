#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import all library


# In[1]:


import requests
import pandas as pd 
from bs4 import BeautifulSoup


# In[2]:


# checking Http response status code 
url="https://www.iplt20.com/auction/2023"
r= requests.get(url)
print(r)


# In[3]:


soup= BeautifulSoup(r.text,"lxml")


# In[4]:


# extracting table data from Html code
table=soup.find("table",class_="ih-td-tab auction-tbl",id="t4")
table


# In[5]:


header=table.find_all("th",class_="skip-filter")
header


# In[6]:


#creating data frame of column name
titles=[]
for i in header:
    title=i.text
    titles.append(title)
df= pd.DataFrame(columns=titles)
df


# In[7]:


#extracting row data from html
rows=table.find_all("tr")
rows


# In[8]:


# inserting row data in Data frame
for i in rows[1:]:
    first_td=i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()
    data=i.find_all("td")[1:]
    row=[tr.text for tr in data]
    row.insert(0,first_td)
    l=len(df)
    df.loc[l]=row
df


# In[ ]:




