#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[3]:


get_ipython().system('pip install requests')


# In[4]:


get_ipython().system('pip install pandas')


# In[232]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[233]:


URL = "https://www.amazon.in/s?k=monitor&ref=nb_sb_noss"


# In[241]:


# Headers for request
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})


# In[242]:


# HTTP Request
webpage = requests.get(URL,headers=HEADERS)


# In[243]:


webpage


# In[191]:


type(webpage.content)


# In[244]:


# Soup Object containiang all data
soup = BeautifulSoup(webpage.content, "html.parser")


# PRODUCT URL

# In[50]:


# # Fetch links as List of Tag Objects
# links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})


# In[60]:


# link=[]

# for i in range(10):
#     link.append(links[i].get('href'))


# In[ ]:


# # list of links
# list


# PRODUCT NAME

# In[72]:


# Fetch Names as List of Tag Objects
# Names = soup.find_all("span", attrs={'class':'a-size-medium a-color-base a-text-normal'})


# In[79]:


# Name=[]

# for i in range(10):
#     Name.append(Names[i].text)


# In[88]:


#list of Names
# Name


# PRODUCT PRICE

# In[82]:


# Fetch Price as List of Tag Objects
# Prices = soup.find_all("span", attrs={'class':'a-price-whole'})


# In[89]:


# Price=[]

# for i in range(10):
#     Price.append(Prices[i].text)


# In[90]:


# list of prices
# Price


# PRODUCT RATING

# In[112]:


# Fetch Price as List of Tag Objects
# Ratings = soup.find_all("div", attrs={'class':'a-row a-size-small'})


# In[117]:


# Ratings[0].text[0:3]


# In[120]:


# Rating=[]

# for i in range(10):
#     Rating.append(Ratings[i].text[0:3])


# In[121]:


# list of ratings
# Rating


# PRODUCT REVIEWS

# In[125]:


# Fetch Price as List of Tag Objects
# Reviews = soup.find_all("span", attrs={'class':'a-size-base s-underline-text'})


# In[127]:


# Reviews[0].text


# In[128]:


# Review=[]

# for i in range(10):
#     Review.append(Reviews[i].text)


# In[129]:


# list of ratings
# Review


# ## function for all items

# In[289]:


link=[]
Name=[]
Price=[]
Rating=[]
Review=[]


# In[290]:


def collector(link,Name,Price,Rating,Review):
    
    # Product URLs
    links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    for i in range(15):
        link.append(links[i].get('href'))
    
    # Product Names
    Names = soup.find_all("span", attrs={'class':'a-size-medium a-color-base a-text-normal'})
    for i in range(15):
        Name.append(Names[i].text)
    
    #product price 
    Prices = soup.find_all("span", attrs={'class':'a-price-whole'})
    for i in range(15):
        Price.append(Prices[i].text)
    
    # Product rating
    Ratings = soup.find_all("div", attrs={'class':'a-row a-size-small'})
    for i in range(15):
        Rating.append(Ratings[i].text[0:3])
    
    # Prodcut reviews
    Reviews = soup.find_all("span", attrs={'class':'a-size-base s-underline-text'})
    for i in range(15):
        Review.append(Reviews[i].text)
    
    


# In[291]:


collector(link,Name,Price,Rating,Review)


# In[292]:


AmazonData=pd.DataFrame()


# In[293]:


AmazonData['URLs']=link
AmazonData['Name'] = Name
AmazonData['Price'] = Price
AmazonData['Rating'] = Rating
AmazonData['Review'] = Review


# In[294]:


AmazonData


# In[ ]:




