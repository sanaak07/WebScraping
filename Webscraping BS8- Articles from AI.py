#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
from bs4 import BeautifulSoup
import requests

#send request to webpage server to get source code of page
page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')

#response 200 means we can scrap data
page 


# In[2]:


soup=BeautifulSoup(page.content)
soup


# In[3]:


#scraping first

f1=soup.find('h2',class_='sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg')
f1
f1.text


# In[4]:


#Scraping multiple 
all1=[]  
for i in soup.find_all('h2',class_='sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg'):
    all1.append(i.text)

all1


# In[5]:


#making dataframe
import pandas as pd
all11=pd.DataFrame({'Paper Title':all1})
all11


# In[6]:


#scraping second

f2=soup.find('span',class_='sc-1w3fpd7-0 dnCnAO')
f2
f2.text


# In[7]:


#Scraping multiple 
all2=[]  
for i in soup.find_all('span',class_='sc-1w3fpd7-0 dnCnAO'):
    all2.append(i.text)

all2


# In[8]:


#making dataframe
import pandas as pd
all22=pd.DataFrame({'Authors':all2})
all22


# In[9]:


#scraping third

f3=soup.find('span',class_='sc-1thf9ly-2 dvggWt')
f3
f3.text


# In[10]:


#Scraping multiple 
all3=[]  
for i in soup.find_all('span',class_='sc-1thf9ly-2 dvggWt'):
    all3.append(i.text)

all3


# In[11]:


#making dataframe
import pandas as pd
all33=pd.DataFrame({'Date Published':all3})
all33


# In[12]:


#concatenate 3 datframes
result = pd.concat([all11, all22,all33], axis=1, join='inner')
display(result)


# In[ ]:




