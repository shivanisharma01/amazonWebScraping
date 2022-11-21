#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
from datetime import date
from datetime import time
import smtplib


# In[5]:


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


# In[6]:


#GET PS4 Details from Amazon Page
URL = "https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/"
webpage = requests.get(URL, headers=HEADERS)


# In[7]:


soup = BeautifulSoup(webpage.content, "lxml")


# In[16]:


# Outer Tag Object
title = soup.find("span", attrs={"id":'productTitle'})
# Inner NavigableString Object
title_value = title.string
# Title as a string value
title_string = title_value.strip()
print("Product Title = ", title_string)


# In[17]:


price=soup.find("span", attrs={"id":"priceblock_ourprice"})
price_value=price.string
price_string=price_value.strip()
print("Product Price= ", price_string)


# In[19]:


review_count= soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
print("Total review:", review_count)


# In[ ]:


#####################################################################################################################
#####################################################################################################################
#####################################################################################################################


# In[24]:


from bs4 import BeautifulSoup
import requests
from datetime import date
from datetime import time
import smtplib


# In[25]:


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


# In[26]:


#GET iPhone 13 Phone Cover Details from Amazon Page
URL = "https://www.amazon.ca/JETech-Compatible-6-1-Inch-Shockproof-Anti-Scratch/dp/B09BTKNGN5/ref=sr_1_5?crid=2XKMZRX9SAGV0&keywords=phone+cover+iphone+13&qid=1664419748&qu=eyJxc2MiOiI1LjY4IiwicXNhIjoiNC44MCIsInFzcCI6IjQuMTAifQ%3D%3D&sprefix=phone+cover+iphone+13%2Caps%2C102&sr=8-5"
webpage = requests.get(URL, headers=HEADERS)


# In[35]:


soup = BeautifulSoup(webpage.content, "lxml")
#print(soup)
soup1 = BeautifulSoup(soup.prettify(),"html.parser")
print(soup1)


# In[67]:


title= soup.find("span", attrs={'id':'productTitle'}).string.strip()


# In[70]:


sale_price=soup.find("span", attrs={'class':'a-offscreen'}).string.strip()


# In[69]:


review_count=soup.find("span",attrs={'id':'acrCustomerReviewText'}).string.strip()


# In[91]:


total_discount=soup.find("span", attrs={'class':'a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'}).string.strip()


# In[98]:


Average_rating=soup.find("span",attrs={'class':'a-icon-alt'}).string.strip()


# In[100]:


print("Product title:",title)
print("Sale Price:",sale_price)
print("Discount %:", total_discount)
print("Product Rating:",Average_rating)
print("Total Reviews:",review_count)


# In[105]:


import datetime
today=datetime.date.today()
print(today)


# In[106]:


import csv

header=['Product','Sale Price','Discount','Rating','Total reviews','Date']
data=[title,sale_price,total_discount,Average_rating,review_count,today]

with open('AmazonWebData.csv','w',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[ ]:




