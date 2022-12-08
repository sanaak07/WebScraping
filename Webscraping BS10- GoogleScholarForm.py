#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
from bs4 import BeautifulSoup
import requests

#send request to webpage server to get source code of page
page=requests.get('https://scholar.google.com/citations?view_op=top_venues&amp;hl=en%3Cbr/%3E')

#response 200 means we can scrap data
page 


# In[2]:


soup=BeautifulSoup(page.content)
soup

