#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
from bs4 import BeautifulSoup
import requests


# # Start scraping data from page 1 (1-50)

# In[2]:


#send request to webpage server to get source code of page
page1=requests.get('https://presidentofindia.nic.in/former-presidents.htm')


# In[3]:


#web scraping response
page1


# In[4]:


#read source code
soup1=BeautifulSoup(page1.content)
soup1


# # Page1 first movie

# In[5]:


#scraping first president name
president1=soup1.find('div',class_='presidentListing')
president1


# In[6]:


#printing first president name
president1.text.split('\n')[1]


# In[7]:


#scraping term of office
termoffice=soup1.find('span',class_='terms')
termoffice.text


# In[8]:


#scraping multiple movies name of first page
presidents = []

for i in soup1.find_all('div',class_='presidentListing'):
    presidents.append(i.text.split('\n')[1])
    
presidents


# In[ ]:




