#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a python program to display IMDB’s Top rated 100 Indian movies’


# In[38]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.imdb.com/list/ls056092300/'

response = requests.get(url)

response


# In[71]:


#Write a python program to scrape details of all the posts

url = 'https://www.patreon.com/coreyms'

response = requests.get(url)
soup = BeautifulSoup(response.content)


headings = []
dates = []
contents = []
likes = []
youtube_links = []

posts = soup.find_all('div', class_='sc-137kp8k-1 lbjiyO')

for post in posts:

    heading = post.find('span',class_='sc-1cvoi1y-0 hxhWXn')
    headings.append(heading)

   
    date = post.find('span',id_='track-click')
    dates.append(date)

    
    content = post.find('div', class_='sc-cfnzm4-0 daxSFj')
    contents.append(content)

    
    like = post.find('span', class_='like-count')
    likes.append(like)

    
    youtube_link = 'No link'
    links = post.find_all('a', href=True)
    for link in links:
        if 'youtube' in link['href']:
            youtube_link = link['href']
            break
    youtube_links.append(youtube_link)


df = pd.DataFrame({
    'Heading': headings,
    'Date': dates,
    'Content': contents,
    'Likes': likes,
    'YouTube Link': youtube_links
})

print(df)


# In[79]:


#Write a python program to scrape first 10 product details which include product name

url = 'https://www.bewakoof.com/bestseller?sort=popular%20'


response = requests.get(url)
soup = BeautifulSoup(response.content)


product_names = []
prices = []
image_urls = []

products = soup.find_all('div', class_='productCardBox', limit=10)

for product in products:
    
    product_name = product.find('h3').text if product.find('h3') else 'No name'
    product_names.append(product_name)
    
   
    price = product.find('div', class_='discountedPriceText').text if product.find('div', class_='discountedPriceText') else 'No price'
    prices.append(price)
    
    
    image_url = product.find('img', class_='productImgTag')['src'] if product.find('img', class_='productImgTag') else 'No image URL'
    image_urls.append(image_url)


df = pd.DataFrame({
    'Product Name': product_names,
    'Price': prices,
    'Image URL': image_urls
})


print(df)


# In[81]:


#Please visit https://www.cnbc.com/world/?region=world and scrap

url = 'https://www.cnbc.com/world/?region=world'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

headings = []
dates = []
links = []

articles = soup.find_all('div', class_='LatestNews-container')


for article in articles:

    heading = article.find('a', class_='LatestNews-headline').text if article.find('a', class_='LatestNews-headline') else 'No headline'
    headings.append(heading)

    date = article.find('time', class_='LatestNews-timestamp').text if article.find('time', class_='LatestNews-timestamp') else 'No date'
    dates.append(date)

    link = article.find('a', class_='LatestNews-headline')['href'] if article.find('a', class_='LatestNews-headline') else 'No link'
    links.append(link)


df = pd.DataFrame({
    'Heading': headings,
    'Date': dates,
    'News Link': links
})

print(df)


# In[82]:


url = 'https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/'


response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

titles = []
dates = []
authors = []

articles = soup.find_all('div', class_='article-content')

for article in articles:

    title = article.find('h2', class_='article-title').text.strip() if article.find('h2', class_='article-title') else 'No title'
    titles.append(title)

    date = article.find('div', class_='article-details').find('span', class_='date').text.strip() if article.find('div', class_='article-details') and article.find('span', class_='date') else 'No date'
    dates.append(date)

    author = article.find('div', class_='article-details').find('span', class_='authors').text.strip() if article.find('div', class_='article-details') and article.find('span', class_='authors') else 'No authors'
    authors.append(author)

# Create a DataFrame
df = pd.DataFrame({
    'Title': titles,
    'Date': dates,
    'Authors': authors
})

print(df)


# In[ ]:




