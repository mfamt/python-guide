---
title: HTML and XML Parsing
ordernum: 1600
references:
  - url: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
  - url: http://www.gregreda.com/2014/07/27/scraping-craigslist-for-tickets/
    title: "Scraping Craigslist for sold out concert tickets"
  - url: http://first-web-scraper.readthedocs.org/en/latest/
    title: "First web scraper"
    description: "A step-by-step guide to writing a web scraper with Python, developed for bootcamps held by Investigative Reporters and Editors. Note: uses Python 2.7"
---



### Installing Beautiful Soup 4


~~~sh
pip install beautifulsoup4
~~~


## Make soup

~~~py
from bs4 import BeautifulSoup
from urllib.request import urlopen
response = urlopen('http://www.example.com')
soup = BeautifulSoup(response.read())  
~~~


## Get all links on a page

~~~sh
links = soup.find_all('a')
len(links)                    # 192
links[0]['href']               
~~~

