#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[18]:


url='https://islamqa.info/en/answers/1/interruption-of-wudhu'


# In[19]:


page=requests.get(url)


# In[20]:


page.content


# In[22]:


soup=BeautifulSoup(page.content,'html.parser')


# In[23]:


soup


# In[24]:


soup.findAll(attrs={'class':'content'})


# In[25]:


qestionanswer=soup.findAll(attrs={'class':'content'})


# In[30]:


question=qestionanswer[0].text.replace('\n'," ")


# In[35]:


summary= soup.find(attrs={'class':'title is-4 is-size-5-touch'}).text.replace('\n'," ")


# In[32]:


questionno= int(soup.find(attrs={'class':'subtitle has-text-weight-bold has-title-case cursor-pointer tooltip'}).text.replace('\n'," "))


# In[33]:


source= soup.find(attrs={'class':'subtitle is-6 has-text-weight-bold is-capitalized'}).text.replace('\n'," ")


# In[37]:


data=[[url,questionno,summary,question,source]]


# In[38]:


data


# In[39]:


df=pd.DataFrame(data,columns=['url','question #','summary','question','sourcce'])


# In[40]:


df


# In[46]:


for i in range(1,10):
    URL='https://islamqa.info/en/answers/'+str(i)
    page=requests.get(URL)
    if(page.status_code==200):
        print('data fetched successfully',i)
        soup=BeautifulSoup(page.content,'html.parser')
        qestionanswer=soup.findAll(attrs={'class':'content'})
        q=qestionanswer[0].text.replace('\n'," ")
        qs=soup.find(attrs={'class':'title is-4 is-size-5-touch'}).text.replace('\n'," ")
        qn=int(soup.find(attrs={'class':'subtitle has-text-weight-bold has-title-case cursor-pointer tooltip'}).text.replace('\n'," "))
        s=soup.find(attrs={'class':'subtitle is-6 has-text-weight-bold is-capitalized'}).text.replace('\n'," ")
        data.insert(qn,[URL,qn,qs,q,s])
    else:
            print('url not found',i)
    df=pd.DataFrame(data,columns=['URL','question #','question','question text','source'])
    df.to_csv('pagedata.csv')


# In[ ]:




