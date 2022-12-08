#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
from bs4 import BeautifulSoup
import requests

#send request to webpage server to get source code of page
page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')

#response 200 means we can scrap data
page 


# In[2]:


soup=BeautifulSoup(page.content)
soup


# In[ ]:





# In[3]:


#scraping first

f1=soup.find('a',class_='restnt-name ellipsis')
f1
f1.text


# In[4]:


#Scraping multiple 
all1=[]  
for i in soup.find_all('a',class_='restnt-name ellipsis'):
    all1.append(i.text)

all1


# In[5]:


#making dataframe
import pandas as pd
all11=pd.DataFrame({'Restaurant Name':all1})
all11


# In[ ]:





# In[6]:


#scraping second

f2=soup.find('span',class_='double-line-ellipsis')
f2
f2.text.split('|')[0]


# In[7]:


#Scraping multiple 
all2=[]  
for i in soup.find_all('span',class_='double-line-ellipsis'):
    all2.append(i.text.split('|')[0])

all2


# In[8]:


#making dataframe
import pandas as pd
all22=pd.DataFrame({'Price':all2})
all22


# In[ ]:





# In[9]:


#scraping third

f3=soup.find('span',class_='double-line-ellipsis')
f3
f3.text.split('|')[1]


# In[10]:


#Scraping multiple 
all3=[]  
for i in soup.find_all('span',class_='double-line-ellipsis'):
    all3.append(i.text.split('|')[1])

all3


# In[11]:


#making dataframe
import pandas as pd
all33=pd.DataFrame({'Cuisine':all3})
all33


# In[ ]:





# In[12]:


#scraping third

f4=soup.find('div',class_='restnt-loc ellipsis')
f4
f4.text


# In[13]:


#Scraping multiple 
all4=[]  
for i in soup.find_all('div',class_='restnt-loc ellipsis'):
    all4.append(i.text)

all4


# In[14]:


#making dataframe
import pandas as pd
all44=pd.DataFrame({'Location':all4})
all44


# In[ ]:





# In[15]:


#scraping third

f5=soup.find('div',class_='restnt-rating rating-4')
f5.text


# In[16]:


#Scraping multiple 
all5=[]  
for i in soup.find_all('div',class_='restnt-rating rating-4'):
    all5.append(i.text)

all5


# In[17]:


#making dataframe
import pandas as pd
all55=pd.DataFrame({'Rating':all5})
all55


# In[ ]:





# In[18]:


#scraping third

f6=soup.find('img',class_='no-img')
f6
f6.text


# In[19]:


#Scraping multiple 
all6=[]  
for i in soup.find_all('img',class_='no-img'):
    all6.append(i.get('data-src'))

all6


# In[20]:


#making dataframe
import pandas as pd
all66=pd.DataFrame({'Image URL':all6})
all66


# In[21]:


#concatenate 3 datframes
result = pd.concat([all11,all22,all33,all44,all55,all66], axis=1, join='inner')
display(result)


# In[ ]:




