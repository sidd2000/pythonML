#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from requests import get


# In[4]:


url = 'http://php.net/'

response = get(url)
#print(response.text[:5000])


# In[7]:


html_soup = BeautifulSoup(response.text, 'html.parser')
#type(html_soup)


# In[8]:


movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
#print(type(movie_containers))
#print(len(movie_containers))


# In[32]:


containers = html_soup.find_all('div', class_ = 'clearfix')
#print(type(containers))
#print(len(containers))


# In[33]:


header_data = containers[1]


# In[34]:


header=header_data.div.div.div.text
#stored header into one string


# In[41]:


#stored bodies of newsletters in one variable
body_containers = html_soup.find_all('div',class_='newscontent')
#print(len(body_containers))


# In[52]:


title_containers = html_soup.find_all('h2',class_='newstitle')
#len(title_containers)
#stored titles in one array


# In[56]:


#storing all titles in an array
title=[]
for container in title_containers:
    title.append(container.text)


# In[58]:


#storing all bodies in an array
body=[]
for contain in body_containers:
    body.append(contain.text)


# In[78]:


file= open("scraped.txt","w")


# In[79]:


file.write(header)


#storing the scraped data in a file
for i in range(0,25):
    file.write(title[i]+"\n"+body[i])


# In[80]:


file.close()


# In[ ]:




