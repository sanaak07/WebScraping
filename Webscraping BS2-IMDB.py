#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
from bs4 import BeautifulSoup
import requests


# # Start scraping data from page 1 (1-50)

# In[2]:


#send request to webpage server to get source code of page
page1=requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')


# In[3]:


#web scraping response
page1


# In[4]:


#read source code
soup1=BeautifulSoup(page1.content)
soup1


# # Page1 first movie

# In[5]:


#scraping first movie name on first page
page1_movie=soup1.find('h3',class_='lister-item-header')
page1_movie


# In[6]:


#printing first movie name on first page
page1_movie.text.split('\n')[2]


# # Page1 first rating

# In[7]:


#scraping first movie rating on first page
page1_rating=soup1.find('div',class_='inline-block ratings-imdb-rating')
page1_rating


# In[8]:


#printing first movie rating on first page
page1_rating.text.split('\n')[2]


# # Page1 first Year of release

# In[9]:


#scraping first movie year of release on first page
page1_yor=soup1.find('span',class_='lister-item-year text-muted unbold')
page1_yor


# In[10]:


#printing first movie year of release on first page
page1_yor.text


# # Page1 movies

# In[11]:


#scraping multiple movies name of first page
page1_movie = []

for i in soup1.find_all('h3',class_='lister-item-header'):
    page1_movie.append(i.text.split('\n')[2])
    
page1_movie


# # Page1 rating

# In[12]:


#scraping multiple movies ratings of first page
page1_rating = []

for i in soup1.find_all('div',class_='inline-block ratings-imdb-rating'):
    page1_rating.append(i.text.split('\n')[2])
    
page1_rating


# # Page1 year of release

# In[13]:


#scraping multiple movies year of release of first page
page1_yor = []

for i in soup1.find_all('span',class_='lister-item-year text-muted unbold'):
    page1_yor.append(i.text)
    
page1_yor


# # Start scraping data from page 2 (51-100)

# In[14]:


#send request to webpage server to get source code of page
page2=requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt')


# In[15]:


#web scraping response
page2


# In[16]:


#read source code
soup2=BeautifulSoup(page2.content)
soup2


# # Page2 movies

# In[17]:


#scraping multiple movies name of second page
page2_movie = []

for i in soup2.find_all('h3',class_='lister-item-header'):
    page2_movie.append(i.text.split('\n')[2])
    
page2_movie


# # Page2 ratings

# In[18]:


#scraping multiple movies ratings of second page
page2_rating = []

for i in soup2.find_all('div',class_='inline-block ratings-imdb-rating'):
    page2_rating.append(i.text.split('\n')[2])
    
page2_rating


# In[19]:


#scraping multiple movies year of release of second page
page2_yor = []

for i in soup2.find_all('span',class_='lister-item-year text-muted unbold'):
    page2_yor.append(i.text)
    
page2_yor


# # Concatenate movies both pages

# In[20]:


#concatinating movies of both pages
all_movies=page1_movie+page2_movie
all_movies


# # Concatenate ratings of both pages

# In[21]:


#concatinating movies ratings of both pages
all_rating=page1_rating+page2_rating
all_rating


# # Concatenate year of release of both pages

# In[22]:


#concatinating movies year of release of both pages
all_yor = page1_yor+page2_yor
all_yor


# # Create Dataframe

# In[23]:


#printing length
print(len(all_movies),len(all_rating),len(all_yor))


# In[24]:


#making dataframe
import pandas as pd
df=pd.DataFrame({'Movies':all_movies,'Ratings':all_rating,'Year of Release':all_yor})
df


# In[ ]:




