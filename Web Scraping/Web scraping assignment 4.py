#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#question 1

import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Wikipedia page to scrape
url = "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"

# Make a request to fetch the content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the most-viewed YouTube videos
table = soup.find("table", {"class": "wikitable"})

# Extract the headers and rows from the table
headers = [header.text.strip() for header in table.find_all("th")]
rows = table.find_all("tr")

# Initialize an empty list to store the data
data = []

# Iterate through the rows and extract the required details
for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) >= 5:
        rank = cols[0].text.strip()
        name = cols[1].text.strip()
        artist = cols[2].text.strip()
        upload_date = cols[4].text.strip()
        views = cols[3].text.strip()
        data.append([rank, name, artist, upload_date, views])

# Convert the data into a pandas DataFrame
columns = ["Rank", "Name", "Artist", "Upload date", "Views"]
youtube_videos_df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(youtube_videos_df)


# In[ ]:


#question 2

# URL of the BCCI home page
base_url = "https://www.bcci.tv"

# Make a request to fetch the content of the BCCI home page
response = requests.get(base_url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the link to the international fixtures page
fixtures_page_url = base_url + soup.find("a", {"title": "Fixtures"}).get("href")

# Make a request to fetch the content of the international fixtures page
response = requests.get(fixtures_page_url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the section containing the fixtures
fixtures_section = soup.find("div", {"class": "js-list"})

# Initialize an empty list to store the data
data = []

# Iterate through the fixtures and extract the required details
fixtures = fixtures_section.find_all("div", {"class": "fixture-card"})
for fixture in fixtures:
    series = fixture.find("h3", {"class": "fixture-card__series"}).text.strip()
    place = fixture.find("p", {"class": "fixture-card__venue"}).text.strip()
    date_time = fixture.find("div", {"class": "fixture-card__datetime"}).text.strip().split(" - ")
    date = date_time[0].strip()
    time = date_time[1].strip() if len(date_time) > 1 else "TBD"
    data.append([series, place, date, time])

# Convert the data into a pandas DataFrame
columns = ["Series", "Place", "Date", "Time"]
fixtures_df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(fixtures_df)


# In[ ]:


#question 3

# URL of the Statisticstimes home page
base_url = "http://statisticstimes.com/"

# Make a request to fetch the content of the Statisticstimes home page
response = requests.get(base_url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the link to the economy page
economy_page_url = base_url + soup.find("a", text="Economy").get("href")

# Make a request to fetch the content of the economy page
response = requests.get(economy_page_url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the link to the Indian states by GDP page
gdp_page_url = base_url + soup.find("a", text="Indian states by GDP").get("href")

# Make a request to fetch the content of the Indian states by GDP page
response = requests.get(gdp_page_url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the state-wise GDP data
table = soup.find("table", {"id": "table_id"})

# Extract the headers and rows from the table
headers = [header.text.strip() for header in table.find_all("th")]
rows = table.find_all("tr")

# Initialize an empty list to store the data
data = []

# Iterate through the rows and extract the required details
for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) >= 6:
        rank = cols[0].text.strip()
        state = cols[1].text.strip()
        gsdp_18_19 = cols[2].text.strip()
        gsdp_19_20 = cols[3].text.strip()
        share_18_19 = cols[4].text.strip()
        gdp_billion = cols[5].text.strip()
        data.append([rank, state, gsdp_18_19, gsdp_19_20, share_18_19, gdp_billion])

# Convert the data into a pandas DataFrame
columns = ["Rank", "State", "GSDP(18-19)- at current prices", "GSDP(19-20)- at current prices", "Share(18-19)", "GDP($ billion)"]
gdp_df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(gdp_df)


# In[ ]:


#question 4

# URL of the GitHub home page
base_url = "https://github.com/"

# Make a request to fetch the content of the GitHub home page
response = requests.get(base_url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the link to the trending page
explore_menu = soup.find("nav", {"aria-label": "Explore GitHub"})
trending_page_url = base_url + explore_menu.find("a", {"href": "/trending"}).get("href")

# Make a request to fetch the content of the trending page
response = requests.get(trending_page_url)
soup = BeautifulSoup(response.content, "html.parser")

# Initialize an empty list to store the data
data = []

# Find all the trending repositories
repos = soup.find_all("article", {"class": "Box-row"})

for repo in repos:
    # Extract repository title
    repo_title = repo.find("h1").text.strip().replace('\n', '').replace(' ', '')

    # Extract repository description
    repo_description = repo.find("p", {"class": "col-9 color-fg-muted my-1 pr-4"}).text.strip() if repo.find("p", {"class": "col-9 color-fg-muted my-1 pr-4"}) else "No description"

    # Extract contributors count
    contributors = repo.find_all("a", {"class": "Link--muted d-inline-block mr-3"})
    contributors_count = len(contributors)

    # Extract language used
    language = repo.find("span", {"itemprop": "programmingLanguage"}).text.strip() if repo.find("span", {"itemprop": "programmingLanguage"}) else "Not specified"

    data.append([repo_title, repo_description, contributors_count, language])

# Convert the data into a pandas DataFrame
columns = ["Repository title", "Repository description", "Contributors count", "Language used"]
trending_repos_df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(trending_repos_df)


# In[ ]:


#question 5

# URL of the Billboard home page
base_url = "https://www.billboard.com/"

# Make a request to fetch the content of the Billboard home page
response = requests.get(base_url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the link to the charts page
charts_page_url = base_url + soup.find("a", {"class": "header__submenu__list__link", "href": "/charts/"}).get("href")

# Make a request to fetch the content of the charts page
response = requests.get(charts_page_url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the link to the Hot 100 page
hot_100_page_url = base_url + soup.find("a", {"class": "header__submenu__list__link", "href": "/charts/hot-100"}).get("href")

# Make a request to fetch the content of the Hot 100 page
response = requests.get(hot_100_page_url)
soup = BeautifulSoup(response.content, "html.parser")

# Initialize an empty list to store the data
data = []

# Find all the songs on the Hot 100 page
songs = soup.find_all("li", {"class": "o-chart-results-list__item"})

for song in songs:
    # Extract song name
    song_name = song.find("h3", {"class": "c-title"}).text.strip()

    # Extract artist name
    artist_name = song.find("span", {"class": "c-label"}).text.strip()

    # Extract last week rank
    last_week_rank = song.find("span", {"class": "c-label--secondary"}).text.strip()

    # Extract peak rank
    peak_rank = song.find("span", {"class": "c-label"}).text.strip()

    # Extract weeks on board
    weeks_on_board = song.find("span", {"class": "c-label--secondary"}).text.strip()

    data.append([song_name, artist_name, last_week_rank, peak_rank, weeks_on_board])

# Convert the data into a pandas DataFrame
columns = ["Song name", "Artist name", "Last week rank", "Peak rank", "Weeks on board"]
top_100_songs_df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(top_100_songs_df)


# In[ ]:


#question 6

# URL of the page to scrape
url = "https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare"

# Make a request to fetch the content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the best-selling books data
table = soup.find("table")

# Extract the headers and rows from the table
headers = [header.text.strip() for header in table.find_all("th")]
rows = table.find_all("tr")

# Initialize an empty list to store the data
data = []

# Iterate through the rows and extract the required details
for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) >= 5:
        book_name = cols[0].text.strip()
        author_name = cols[1].text.strip()
        volumes_sold = cols[2].text.strip()
        publisher = cols[3].text.strip()
        genre = cols[4].text.strip()
        data.append([book_name, author_name, volumes_sold, publisher, genre])

# Convert the data into a pandas DataFrame
columns = ["Book name", "Author name", "Volumes sold", "Publisher", "Genre"]
books_df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(books_df)


# In[ ]:


#question 7

# URL of the IMDb page to scrape
url = "https://www.imdb.com/list/ls095964455/"

# Make a request to fetch the content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Initialize an empty list to store the data
data = []

# Find all the TV series items on the page
tv_series_list = soup.find_all("div", class_="lister-item mode-detail")

for tv_series in tv_series_list:
    # Extract name
    name = tv_series.find("h3", class_="lister-item-header").find("a").text.strip()

    # Extract year span
    year_span = tv_series.find("span", class_="lister-item-year").text.strip()

    # Extract genre
    genre = tv_series.find("span", class_="genre").text.strip() if tv_series.find("span", class_="genre") else "Not specified"

    # Extract run time
    runtime = tv_series.find("span", class_="runtime").text.strip() if tv_series.find("span", class_="runtime") else "Not specified"

    # Extract ratings
    ratings = tv_series.find("span", class_="ipl-rating-star__rating").text.strip() if tv_series.find("span", class_="ipl-rating-star__rating") else "Not specified"

    # Extract votes
    votes = tv_series.find("span", {"name": "nv"}).text.strip() if tv_series.find("span", {"name": "nv"}) else "Not specified"

    data.append([name, year_span, genre, runtime, ratings, votes])

# Convert the data into a pandas DataFrame
columns = ["Name", "Year span", "Genre", "Run time", "Ratings", "Votes"]
tv_series_df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(tv_series_df)


# In[ ]:


#question 8

# URL of the UCI Machine Learning Repository home page
base_url = "https://archive.ics.uci.edu/ml/index.php"

# Make a request to fetch the content of the UCI Machine Learning Repository home page
response = requests.get(base_url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the link to the Show All Dataset page
show_all_datasets_link = soup.find("a", text="View All Collections of Data Sets")

# Construct the full URL for the Show All Dataset page
show_all_datasets_url = "https://archive.ics.uci.edu/ml/datasets.php"

# Make a request to fetch the content of the Show All Dataset page
response = requests.get(show_all_datasets_url)
soup = BeautifulSoup(response.content, "html.parser")

# Initialize an empty list to store the data
data = []

# Find the table containing the datasets
table = soup.find("table", {"cellpadding": "3"})

# Iterate through the rows and extract the required details
for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    if len(cols) >= 7:
        dataset_name = cols[0].text.strip()
        data_type = cols[1].text.strip()
        task = cols[2].text.strip()
        attribute_type = cols[3].text.strip()
        no_of_instances = cols[4].text.strip()
        no_of_attributes = cols[5].text.strip()
        year = cols[6].text.strip()
        data.append([dataset_name, data_type, task, attribute_type, no_of_instances, no_of_attributes, year])

# Convert the data into a pandas DataFrame
columns = ["Dataset name", "Data type", "Task", "Attribute type", "No of instances", "No of attributes", "Year"]
datasets_df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(datasets_df)

