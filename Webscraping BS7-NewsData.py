#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
from bs4 import BeautifulSoup
import requests

#send request to webpage server to get source code of page
page=requests.get('https://www.cnbc.com/world/?region=world')

#response 200 means we can scrap data
page   


# In[2]:


soup=BeautifulSoup(page.content)
soup


# In[3]:


#scraping first

f1=soup.find('div',class_='RiverHeadline-headline RiverHeadline-hasThumbnail')
f1
f1.text


# In[4]:


#Scraping multiple 
all1=[]  
for i in soup.find_all('div',class_='RiverHeadline-headline RiverHeadline-hasThumbnail'):
    all1.append(i.text)

all1


# In[5]:


#making dataframe
import pandas as pd
all11=pd.DataFrame({'Headline':all1})
all11


# In[6]:


#scraping second

f2=soup.find('span',class_='RiverByline-datePublished')
f2
f2.text


# In[7]:


#Scraping multiple 
all2=[]  
for i in soup.find_all('span',class_='RiverByline-datePublished'):
    all2.append(i.text)

all2


# In[8]:


#making dataframe
import pandas as pd
all22=pd.DataFrame({'Time':all2})
all22


# In[9]:


#concatenate 2 datframes
result = pd.concat([all11, all22], axis=1, join='inner')
display(result)


# In[ ]:




