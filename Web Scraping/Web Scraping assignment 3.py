#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Exercise 1

import requests
from bs4 import BeautifulSoup

def get_amazon_search_results(search_query):
    # Replace spaces in search query with '+' to form a proper URL
    search_query = search_query.replace(' ', '+')
    url = f'https://www.amazon.in/s?k={search_query}'
    
    # Send a GET request to the Amazon search URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all product listings on the search results page
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    
    # Extract and print product details
    for product in products:
        title = product.find('span', {'class': 'a-size-medium a-color-base a-text-normal'})
        price = product.find('span', {'class': 'a-price-whole'})
        rating = product.find('span', {'class': 'a-icon-alt'})
        
        # If any detail is missing, replace it with a hyphen
        title = title.text.strip() if title else '-'
        price = price.text.strip() if price else '-'
        rating = rating.text.strip() if rating else '-'
        
        print(f'Title: {title}')
        print(f'Price: {price}')
        print(f'Rating: {rating}')
        print('-' * 50)


# In[ ]:


#Exercise 2

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_amazon_search_results(search_query, max_pages=3):
    search_query = search_query.replace(' ', '+')
    base_url = 'https://www.amazon.in/s'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    all_products = []

    for page in range(1, max_pages + 1):
        url = f'{base_url}?k={search_query}&page={page}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        if not products:  # No more products
            break

        for product in products:
            title = product.find('span', {'class': 'a-size-medium a-color-base a-text-normal'})
            price = product.find('span', {'class': 'a-price-whole'})
            product_url = product.find('a', {'class': 'a-link-normal s-no-outline'})
            product_page_url = 'https://www.amazon.in' + product_url['href'] if product_url else '-'
            
            # Go to the product page to extract more details
            if product_page_url != '-':
                product_response = requests.get(product_page_url, headers=headers)
                product_soup = BeautifulSoup(product_response.content, 'html.parser')
                
                brand = product_soup.find('a', {'id': 'bylineInfo'})
                return_exchange = product_soup.find('a', {'id': 'RETURNS_POLICY'})
                expected_delivery = product_soup.find('div', {'id': 'ddmDeliveryMessage'})
                availability = product_soup.find('div', {'id': 'availability'})

                brand = brand.text.strip() if brand else '-'
                return_exchange = return_exchange.text.strip() if return_exchange else '-'
                expected_delivery = expected_delivery.text.strip() if expected_delivery else '-'
                availability = availability.text.strip() if availability else '-'
            else:
                brand = '-'
                return_exchange = '-'
                expected_delivery = '-'
                availability = '-'

            # If any detail is missing, replace it with a hyphen
            title = title.text.strip() if title else '-'
            price = price.text.strip() if price else '-'
            product_page_url = product_page_url if product_page_url else '-'

            all_products.append({
                'Brand Name': brand,
                'Name of the Product': title,
                'Price': price,
                'Return/Exchange': return_exchange,
                'Expected Delivery': expected_delivery,
                'Availability': availability,
                'Product URL': product_page_url
            })

    return all_products

df = pd.DataFrame(products)
df.to_csv(f'{search_query}_amazon_products.csv', index=False)


# In[4]:


#Exercise 3

import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def download_image(url, folder, image_name):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(os.path.join(folder, image_name), 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
    except Exception as e:
        print(f'Could not download {image_name}: {e}')

def search_and_download_images(keywords, num_images=10):
    # Create a folder for the images
    if not os.path.exists('images'):
        os.makedirs('images')
    
    # Set up the Selenium WebDriver (using Chrome in this example)
    driver = webdriver.Chrome()

    for keyword in keywords:
        print(f'Searching for {keyword}...')
        driver.get('https://images.google.com/')
        
        # Find the search bar and enter the keyword
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)
        
        # Scroll down to load more images
        time.sleep(2)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        image_elements = soup.find_all('img', {'class': 'rg_i Q4LuWd'}, limit=num_images)
        
        # Create a folder for the current keyword
        keyword_folder = os.path.join('images', keyword.replace(' ', '_'))
        if not os.path.exists(keyword_folder):
            os.makedirs(keyword_folder)

        # Download the images
        for i, img in enumerate(image_elements):
            try:
                img_url = img['src']
                if img_url.startswith('http'):
                    download_image(img_url, keyword_folder, f'{keyword}_{i+1}.jpg')
            except KeyError:
                continue
        
        print(f'Downloaded {len(image_elements)} images for {keyword}')
    
    driver.quit()

if __name__ == '__main__':
    keywords = ['fruits', 'cars', 'Machine Learning', 'Guitar', 'Cakes']
    search_and_download_images(keywords)


# In[ ]:


#Exercise 4

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_flipkart_smartphone_details(search_query):
    # Set up Selenium WebDriver (using Chrome)
    driver = webdriver.Chrome()
    driver.get('https://www.flipkart.com/')
    
    # Close the login pop-up if it appears
    try:
        close_button = driver.find_element(By.XPATH, '//button[text()="✕"]')
        close_button.click()
    except:
        pass
    
    # Find the search bar and enter the search query
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(3)  # Allow time for the page to load
    
    # Parse the search results
    products = driver.find_elements(By.CLASS_NAME, '_1AtVbE')
    
    smartphone_details = []

    for product in products:
        try:
            name = product.find_element(By.CLASS_NAME, '_4rR01T').text
            link = product.find_element(By.CSS_SELECTOR, 'a._1fQZEK').get_attribute('href')
            price = product.find_element(By.CLASS_NAME, '_30jeq3').text
            details = product.find_elements(By.CLASS_NAME, 'rgWa7D')
            
            specs = {
                'Brand Name': name.split()[0],
                'Smartphone name': name,
                'Colour': '-',
                'RAM': '-',
                'Storage(ROM)': '-',
                'Primary Camera': '-',
                'Secondary Camera': '-',
                'Display Size': '-',
                'Battery Capacity': '-',
                'Price': price,
                'Product URL': link
            }

            for detail in details:
                text = detail.text
                if 'RAM' in text and 'ROM' in text:
                    specs['RAM'], specs['Storage(ROM)'] = text.split('|')
                elif 'Display' in text:
                    specs['Display Size'] = text.split(':')[1].strip()
                elif 'Battery' in text:
                    specs['Battery Capacity'] = text.split(':')[1].strip()
                elif 'Primary Camera' in text:
                    specs['Primary Camera'] = text.split(':')[1].strip()
                elif 'Secondary Camera' in text:
                    specs['Secondary Camera'] = text.split(':')[1].strip()
                elif 'Color' in text:
                    specs['Colour'] = text.split(':')[1].strip()

            smartphone_details.append(specs)
        except Exception as e:
            print(f"Error parsing product: {e}")
            continue

    driver.quit()
    return smartphone_details

if __name__ == '__main__':
    search_query = input('Enter the smartphone to search on Flipkart: ')
    smartphones = get_flipkart_smartphone_details(search_query)
    
    # Create a DataFrame and save to CSV
    df = pd.DataFrame(smartphones)
    df.to_csv(f'{search_query}_flipkart_smartphones.csv', index=False)
    print(f'Scraped data saved to {search_query}_flipkart_smartphones.csv')


# In[ ]:


#Exercise 5

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_coordinates(city_name):
    # Set up the Selenium WebDriver (using Chrome in this example)
    driver = webdriver.Chrome()
    
    # Navigate to Google Maps
    driver.get('https://maps.google.com')
    
    # Find the search bar and enter the city name
    search_box = driver.find_element(By.ID, 'searchboxinput')
    search_box.send_keys(city_name)
    search_box.send_keys(Keys.RETURN)
    
    # Allow time for the page to load and URL to update
    time.sleep(5)
    
    # Extract the URL and parse the coordinates from it
    url = driver.current_url
    
    driver.quit()
    
    # Extract coordinates from the URL
    try:
        coords = url.split('@')[1].split(',')[0:2]
        latitude = coords[0]
        longitude = coords[1]
        return latitude, longitude
    except Exception as e:
        print(f"Error extracting coordinates: {e}")
        return None, None

if __name__ == '__main__':
    city_name = input('Enter the city name to search on Google Maps: ')
    latitude, longitude = get_coordinates(city_name)
    
    if latitude and longitude:
        print(f'Coordinates of {city_name}:')
        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')
    else:
        print('Could not extract coordinates.')


# In[ ]:


#Exercise 6

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_best_gaming_laptops():
    url = 'https://www.digit.in/top-products/best-gaming-laptops-40.html'  # URL of the page to scrape
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the container with the list of best gaming laptops
    laptops_container = soup.find('div', {'class': 'TopNumbeHeading'}).parent
    
    laptops = []
    
    for laptop in laptops_container.find_all('div', {'class': 'TopNumbeBox'}):
        name = laptop.find('h2').text.strip()
        details = laptop.find_all('div', {'class': 'Spcs-details'})
        
        specs = {
            'Name': name,
            'Processor': '-',
            'Graphics Card': '-',
            'RAM': '-',
            'Storage': '-',
            'Display': '-',
            'Price': '-'
        }
        
        for detail in details:
            detail_text = detail.text.strip()
            if 'Processor' in detail_text:
                specs['Processor'] = detail_text.split(':')[-1].strip()
            elif 'Graphics Processor' in detail_text:
                specs['Graphics Card'] = detail_text.split(':')[-1].strip()
            elif 'Memory' in detail_text:
                specs['RAM'] = detail_text.split(':')[-1].strip()
            elif 'Storage' in detail_text:
                specs['Storage'] = detail_text.split(':')[-1].strip()
            elif 'Display' in detail_text:
                specs['Display'] = detail_text.split(':')[-1].strip()
            elif 'Price' in detail_text:
                specs['Price'] = detail_text.split(':')[-1].strip()
        
        laptops.append(specs)
    
    return laptops

if __name__ == '__main__':
    laptops = get_best_gaming_laptops()
    
    # Create a DataFrame and save to CSV
    df = pd.DataFrame(laptops)
    df.to_csv('best_gaming_laptops.csv', index=False)
    print('Scraped data saved to best_gaming_laptops.csv')


# In[ ]:


#exercise 7

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_billionaires_details():
    url = 'https://www.forbes.com/billionaires/'  # URL of the page to scrape
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the container with the list of billionaires
    table = soup.find('table')
    
    billionaires = []

    # Check if table exists and find all rows
    if table:
        rows = table.find_all('tr')[1:]  # Skip the header row
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) < 7:
                continue
            
            rank = cols[0].text.strip()
            name = cols[1].text.strip()
            net_worth = cols[2].text.strip()
            age = cols[3].text.strip() if cols[3].text.strip() else '-'
            citizenship = cols[4].text.strip()
            source = cols[5].text.strip()
            industry = cols[6].text.strip()
            
            billionaires.append({
                'Rank': rank,
                'Name': name,
                'Net worth': net_worth,
                'Age': age,
                'Citizenship': citizenship,
                'Source': source,
                'Industry': industry
            })
    
    return billionaires

if __name__ == '__main__':
    billionaires = get_billionaires_details()
    
    # Create a DataFrame and save to CSV
    df = pd.DataFrame(billionaires)
    df.to_csv('forbes_billionaires.csv', index=False)
    print('Scraped data saved to forbes_billionaires.csv')


# In[ ]:


#exercise 8

import os
import googleapiclient.discovery
import pandas as pd

def get_youtube_comments(video_id, api_key, max_results=500):
    # Disable OAuthlib's HTTPS verification when running locally.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # Build the YouTube API client
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    comments = []
    next_page_token = None

    while len(comments) < max_results:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            pageToken=next_page_token,
            maxResults=100
        )
        response = request.execute()
        
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "Comment": comment["textDisplay"],
                "Upvotes": comment["likeCount"],
                "Posted Time": comment["publishedAt"]
            })

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return comments[:max_results]

if __name__ == '__main__':
    api_key = "YOUR_API_KEY"
    video_id = input("Enter the YouTube video ID: ")
    max_results = 500

    comments = get_youtube_comments(video_id, api_key, max_results)

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(comments)
    df.to_csv('youtube_comments.csv', index=False)
    print('Scraped data saved to youtube_comments.csv')


# In[ ]:


#exercise 9

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_hostel_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    name = soup.find('h1', class_='detailheader__name').text.strip()
    distance = soup.find('span', class_='detailheader__distance').text.strip()
    rating = soup.find('div', class_='score orange').text.strip() if soup.find('div', class_='score orange') else '-'
    total_reviews = soup.find('span', class_='reviews').text.strip() if soup.find('span', class_='reviews') else '-'
    overall_reviews = soup.find('div', class_='keyword').text.strip() if soup.find('div', class_='keyword') else '-'
    
    prices = soup.find_all('div', class_='price')
    privates_price = prices[0].text.strip() if len(prices) > 0 else '-'
    dorms_price = prices[1].text.strip() if len(prices) > 1 else '-'
    
    facilities = soup.find_all('div', class_='facilities-container__facility')
    facilities_list = [facility.text.strip() for facility in facilities]
    
    property_description = soup.find('div', class_='content collapse-content').text.strip() if soup.find('div', class_='content collapse-content') else '-'
    
    hostel_details = {
        'Hostel Name': name,
        'Distance from City Centre': distance,
        'Rating': rating,
        'Total Reviews': total_reviews,
        'Overall Reviews': overall_reviews,
        'Privates From Price': privates_price,
        'Dorms From Price': dorms_price,
        'Facilities': ', '.join(facilities_list),
        'Property Description': property_description
    }
    
    return hostel_details

def scrape_hostelworld_london():
    base_url = 'https://www.hostelworld.com'
    search_url = f'{base_url}/findabed.php/ChosenCity.London/ChosenCountry.England'
    
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    hostels = []
    
    # Find total number of pages
    pagination = soup.find('ul', class_='pagination')
    if pagination:
        total_pages = int(pagination.find_all('li')[-2].text.strip())
    else:
        total_pages = 1
    
    for page in range(1, total_pages + 1):
        response = requests.get(f'{search_url}/page/{page}')
        soup = BeautifulSoup(response.content, 'html.parser')
        
        hostel_cards = soup.find_all('div', class_='property-card')
        
        for hostel_card in hostel_cards:
            hostel_url = base_url + hostel_card.find('a', class_='property-card__link').get('href')
            hostel_details = get_hostel_details(hostel_url)
            hostels.append(hostel_details)
    
    return hostels

if __name__ == '__main__':
    hostels = scrape_hostelworld_london()
    
    # Create a DataFrame and save to CSV
    df = pd.DataFrame(hostels)
    df.to_csv('london_hostels.csv', index=False)
    print('Scraped data saved to london_hostels.csv')

